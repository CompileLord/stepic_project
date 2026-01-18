import subprocess
from .models import Task, OutputInput

def check_and_run_command(user_code, task_id):
    task = Task.objects.get(id=task_id)
    test_cases = task.output_inputs.all()

    for case in test_cases:
        try:
            full_script = f"import sys; sys.stdin = sys.stdin; {user_code}"
            
            process = subprocess.run(
                ['python3', '-c', full_script],
                input=case.input,
                capture_output=True,
                text=True,
                timeout=5
            )

            if process.returncode != 0:
                return f"Runtime Error:\n{process.stderr}"

            actual_output = process.stdout.strip()
            expected_output = case.output.strip()

            if actual_output != expected_output:
                return f"Incorrect.\nInput: {case.input}\nExpected: {expected_output}\nGot: {actual_output}"

        except subprocess.TimeoutExpired:
            return "Error: Time Limit Exceeded"
        except Exception as e:
            return f"System Error: {str(e)}"

    return "Correct"
