class Graphics:
    def __init__(self, ctx, shader_program, vertices, indices):
        self.ctx = ctx
        self.shader_program = shader_program
        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.ibo = self.ctx.buffer(indices.tobytes())
        self.vao = self.ctx.vertex_array(shader_program.program, [
            (self.vbo,'3f 3f','in_pos','in_color')
        ], self.ibo)
        
    def set_shader(self, shader_program):
        self.shader_program = shader_program
    
    def set_uniform(self, name, value):
        self.shader_program.set_uniform(name, value)

