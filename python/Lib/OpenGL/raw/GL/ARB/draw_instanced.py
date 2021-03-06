'''OpenGL extension ARB.draw_instanced

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_draw_instanced'
_DEPRECATED = False

glDrawArraysInstancedARB = platform.createExtensionFunction( 
'glDrawArraysInstancedARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLsizei,constants.GLsizei,),
doc='glDrawArraysInstancedARB(GLenum(mode), GLint(first), GLsizei(count), GLsizei(primcount)) -> None',
argNames=('mode','first','count','primcount',),
deprecated=_DEPRECATED,
)

glDrawElementsInstancedARB = platform.createExtensionFunction( 
'glDrawElementsInstancedARB',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLenum,ctypes.c_void_p,constants.GLsizei,),
doc='glDrawElementsInstancedARB(GLenum(mode), GLsizei(count), GLenum(type), c_void_p(indices), GLsizei(primcount)) -> None',
argNames=('mode','count','type','indices','primcount',),
deprecated=_DEPRECATED,
)


def glInitDrawInstancedARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
