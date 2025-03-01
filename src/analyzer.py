import timeit

def analyze_code(code_str: str):
    try:
        exec_time = timeit.timeit(code_str, number=1000)
        return {"execution_time": exec_time}
    except Exception as e:
        return {"error": str(e)}