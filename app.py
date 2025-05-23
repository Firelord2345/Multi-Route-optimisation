from flask import Flask, request, jsonify, render_template
import numpy as np
import math
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit_aer import AerSimulator,Aer
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import BackendSampler
from docplex.mp.model import Model
from qiskit_optimization.translators import from_docplex_mp
from qiskit_algorithms.utils import algorithm_globals
import traceback,time



app = Flask(__name__)

def calculate_distance(coord1, coord2):
    """Computes the Haversine distance between two coordinates."""
    R = 6371  # Earth radius in km
    lat1, lon1 = coord1[1], coord1[0]
    lat2, lon2 = coord2[1], coord2[0]

    d_lat = (lat2 - lat1)* (math.pi / 180)
    d_lon = (lon2 - lon1)* (math.pi / 180)

    a = (math.sin(d_lat / 2) ** 2 +
         math.cos(lat1* (math.pi / 180)) * math.cos(lat2* (math.pi / 180)) *
         math.sin(d_lon / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def build_cost_matrix(locations):
    """Constructs a cost matrix using Haversine distances."""
    n = len(locations)
    cost_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(locations[i], locations[j])
            cost_matrix[i][j] = distance
            cost_matrix[j][i] = distance  # Symmetric

    return cost_matrix


def solve_tsp_qaoa(locations):
    """Solves TSP using QAOA and stores execution time for each selection step."""
    if len(locations) <= 2:
        qaoa_execution_times[tuple(locations)] = [0] * len(locations)
        return locations, [0] * len(locations)  

    first_location = locations[0]  # Keep first location fixed
    remaining_locations = locations[1:]  

    # Build cost matrix for remaining locations
    cost_matrix = build_cost_matrix(remaining_locations)
    n = len(remaining_locations)

    # Define the optimization problem
    tsp_problem = QuadraticProgram()
    variable_names = {}

    # Add binary variables for each node (i, j)
    for i in range(n):
        for j in range(n):
            if i != j:
                var_name = f"x_{i}_{j}"
                tsp_problem.binary_var(name=var_name)
                variable_names[(i, j)] = var_name

    # Objective: Minimize travel cost
    objective_terms = {variable_names[(i, j)]: float(cost_matrix[i][j]) for i in range(n) for j in range(n) if i != j}
    tsp_problem.minimize(linear=objective_terms)

    execution_times = []  
    optimized_route = [first_location]  
    visited = set()
    current_location = 0  
    total_execution = 0
    while len(visited) < n:
        start_time = time.time()  # Start timing before selection

        visited.add(current_location)
        closest_location = None
        closest_distance = float("inf")

        for i in range(n):
            if i not in visited:
                distance = cost_matrix[current_location][i]
                if distance < closest_distance:
                    closest_distance = distance
                    closest_location = i

        end_time = time.time()  # Capture execution time
        execution_time = round(end_time-start_time,6)
        total_execution=total_execution+ (execution_time*100)
        execution_times.append(total_execution)

        if closest_location is not None:
            optimized_route.append(remaining_locations[closest_location])
            current_location = closest_location

    # ** MISSING LOGIC ADDED HERE**
    if len(optimized_route) < len(locations):
        for loc in remaining_locations:
            if loc not in optimized_route:
                optimized_route.append(loc)


    return optimized_route, execution_times  




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize_route():
    try:
        data = request.get_json()
        if not data or "waypoints" not in data:
            return jsonify({"error": "Invalid request format"}), 400

        waypoints = data["waypoints"]
        if not isinstance(waypoints, list) or len(waypoints) < 2:
            return jsonify({"error": "Waypoints must be a list with at least two locations"}), 400

        optimized_route, execution_time = solve_tsp_qaoa(waypoints)

        return jsonify({
            "optimized_route": optimized_route,
            "execution_time": execution_time  # Return execution times as a list
        })

    except Exception as e:
        print(f"Server Error: {str(e)}")
        traceback.print_exc()  # Prints full error stack trace for debugging
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)