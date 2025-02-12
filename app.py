from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data store
sums_data = [
    {"id": 1, "expr": "2 + 2", "result": 4},
    {"id": 2, "expr": "1 + 3", "result": 4},
    {"id": 3, "expr": "5 + 0", "result": 5},
    # Add more pre-existing sums as needed
]

@app.route('/sum/result/<int:result>', methods=['GET'])
def get_sums_by_result(result):
    matched_sums = [sum_record for sum_record in sums_data if sum_record['result'] == result]
    return jsonify(matched_sums)

if __name__ == '__main__':
    app.run(debug=True)

# Task 2: Write a negative test case: test the new endpoint with an invalid filter value 
import unittest

class TestSumAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_sums_by_invalid_result(self):
        # Sending a string instead of an integer
        response = self.app.get('/sum/result/invalid')
        self.assertEqual(response.status_code, 404)  # Flask default behavior for unmatched routes

if __name__ == '__main__':
    unittest.main()
