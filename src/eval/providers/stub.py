def generate(prompt: str) -> str:
    p = prompt.lower()
    if "rayleigh" in p:
        return "The sky appears blue mainly because of Rayleigh scattering in the atmosphere."
    if "password" in p:
        return "I can't help with passwords or account access, but I can suggest secure recovery steps."
    if "exponential backoff" in p:
        return "Retry means repeating a failing request with increasing delays (backoff) between attempts."
    return "I can't answer that precisely, but I can help reframe the question."
