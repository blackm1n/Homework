# Упс, опять однострочник

def reverse_keys(**kwargs) -> dict:
    return {v if v.__hash__ else str(v): k for k, v in kwargs.items()}


print(reverse_keys(hello=1, hello2=2, something=['hello']))
