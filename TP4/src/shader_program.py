import numpy as np

class ShaderProgram:
    def __init__(self, ctx, vertex_shader_path, fragment_shader_path):
        with open (vertex_shader_path) as file:
            vertex_shader = file.read()
        with open (fragment_shader_path) as file:
            fragment_shader = file.read()
        self.program = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
    
    def set_uniform(self, name, value):
        if name in self.program:
            if hasattr(value, "to_list"): 
                value = np.array(value.to_list(), dtype="f4")
            elif isinstance(value, (list, tuple)):
                value = np.array(value, dtype="f4")
            self.program[name].write(value.tobytes())
        else:
            print(f"Warning: Uniform '{name}' not found in shader program.")
