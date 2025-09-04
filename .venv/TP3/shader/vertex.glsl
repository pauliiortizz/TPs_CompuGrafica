#version 330

in vec2 in_pos;
out vec2 fragCoord;

void main() {
    fragCoord = in_pos;
    gl_Position = vec4(in_pos, 0.0, 1.0);
}
