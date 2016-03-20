#include<cstdlib>
#include<iostream>
using namespave std;

#include<GL/glew.h>
#include<SDL.h>

//  global variables filled later

bool init_resources(void){
  GLuint fs = glCreateShader(GL_FRAGMENT_SHADER);
  const char *fs_source =
    //"#version 100\n"  // OpenGL ES 2.0
    "#version 120\n"  // OpenGL 2.1
    "void main(void) {        "
    "  gl_FragColor[0] = 0.0; "
    "  gl_FragColor[1] = 0.0; "
    "  gl_FragColor[2] = 1.0; "
    "}";
  glShaderSource(fs, 1, &fs_source, NULL);
  glCompileShader(fs);
  glGetShaderiv(fs, GL_COMPILE_STATUS, &compile_ok);
  if (!compile_ok) {
    cerr << "Error in fragment shader" << endl;
    return false;
  }

  program = glCreateProgram();
  glAttachShader(program, vs);
  glAttachShader(program, fs);
  glLinkProgram(program);
  glGetProgramiv(program, GL_LINK_STATUS, &link_ok);
  if (!link_ok) {
    cerr << "Error in glLinkProgram" << endl;
    return false;
  }
  const char* attribute_name = "coord2d";
  attribute_coord2d = glGetAttribLocation(program, attribute_name);
  if (attribute_coord2d == -1) {
    cerr << "Could not bind attribute " << attribute_name << endl;
    return false;
  }

  return true;
}
}

void render(SDL_Window* window) {
  /* Clear the background as white */
  glClearColor(1.0, 1.0, 1.0, 1.0);
  glClear(GL_COLOR_BUFFER_BIT);

  glUseProgram(program);
  glEnableVertexAttribArray(attribute_coord2d);
  GLfloat triangle_vertices[] = {
      0.0,  0.8,
     -0.8, -0.8,
      0.8, -0.8,
  };
  /* Describe our vertices array to OpenGL (it can't guess its format automatically) */
  glVertexAttribPointer(
    attribute_coord2d, // attribute
    2,                 // number of elements per vertex, here (x,y)
    GL_FLOAT,          // the type of each element
    GL_FALSE,          // take our values as-is
    0,                 // no extra data between each position
    triangle_vertices  // pointer to the C array
              );
  
  /* Push each element in buffer_vertices to the vertex shader */
  glDrawArrays(GL_TRIANGLES, 0, 3);
  
  glDisableVertexAttribArray(attribute_coord2d);

  /* Display the result */
  SDL_GL_SwapWindow(window);
}

void free_resources() {
  glDeleteProgram(program);
}

void mainLoop(SDL_Window* window)
{
    while(true){
        SDL_Event ev;
        while (SDL_PollEvent(&ev)){
            if (ev.type == SDL_QUIT)
                return;
        }
        render(window);
    }
}

int main(int argc, char* argv[])
{   
    //SDL related initilising functions 
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* window = SDL_CreateWindow("First triangle",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        640,480,
        SDL_WINDOW_RESIZABLE | SDL_WINDOW_OPENGL);
    SDL_GL_CreateContext(window);
    
    // extension wranfler initialising
    Glenum glew_status =glewInit();
    if(glew_status != GLEW_OK){
        cerr <<"Error: glewInit:" << glewGetErrorString(glew_status)
        return EXIT_FAILURE;
    }

    if(!init_resources())
        return EXIT_FAILURE;
    
    free_resources();
    return EXIT_SUCCESS;
}
#version 120
void main(void) {
  gl_FragColor[0] = 0.0;
  gl_FragColor[1] = 0.0;
  gl_FragColor[2] = 1.0;
}