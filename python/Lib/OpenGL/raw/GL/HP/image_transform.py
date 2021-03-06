'''OpenGL extension HP.image_transform

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_HP_image_transform'
_DEPRECATED = False
GL_IMAGE_SCALE_X_HP = constant.Constant( 'GL_IMAGE_SCALE_X_HP', 0x8155 )
GL_IMAGE_SCALE_Y_HP = constant.Constant( 'GL_IMAGE_SCALE_Y_HP', 0x8156 )
GL_IMAGE_TRANSLATE_X_HP = constant.Constant( 'GL_IMAGE_TRANSLATE_X_HP', 0x8157 )
GL_IMAGE_TRANSLATE_Y_HP = constant.Constant( 'GL_IMAGE_TRANSLATE_Y_HP', 0x8158 )
GL_IMAGE_ROTATE_ANGLE_HP = constant.Constant( 'GL_IMAGE_ROTATE_ANGLE_HP', 0x8159 )
GL_IMAGE_ROTATE_ORIGIN_X_HP = constant.Constant( 'GL_IMAGE_ROTATE_ORIGIN_X_HP', 0x815A )
GL_IMAGE_ROTATE_ORIGIN_Y_HP = constant.Constant( 'GL_IMAGE_ROTATE_ORIGIN_Y_HP', 0x815B )
GL_IMAGE_MAG_FILTER_HP = constant.Constant( 'GL_IMAGE_MAG_FILTER_HP', 0x815C )
GL_IMAGE_MIN_FILTER_HP = constant.Constant( 'GL_IMAGE_MIN_FILTER_HP', 0x815D )
GL_IMAGE_CUBIC_WEIGHT_HP = constant.Constant( 'GL_IMAGE_CUBIC_WEIGHT_HP', 0x815E )
GL_CUBIC_HP = constant.Constant( 'GL_CUBIC_HP', 0x815F )
GL_AVERAGE_HP = constant.Constant( 'GL_AVERAGE_HP', 0x8160 )
GL_IMAGE_TRANSFORM_2D_HP = constant.Constant( 'GL_IMAGE_TRANSFORM_2D_HP', 0x8161 )
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = constant.Constant( 'GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP', 0x8162 )
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = constant.Constant( 'GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP', 0x8163 )
glImageTransformParameteriHP = platform.createExtensionFunction( 
'glImageTransformParameteriHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,),
doc='glImageTransformParameteriHP(GLenum(target), GLenum(pname), GLint(param)) -> None',
argNames=('target','pname','param',),
deprecated=_DEPRECATED,
)

glImageTransformParameterfHP = platform.createExtensionFunction( 
'glImageTransformParameterfHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLfloat,),
doc='glImageTransformParameterfHP(GLenum(target), GLenum(pname), GLfloat(param)) -> None',
argNames=('target','pname','param',),
deprecated=_DEPRECATED,
)

glImageTransformParameterivHP = platform.createExtensionFunction( 
'glImageTransformParameterivHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glImageTransformParameterivHP(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glImageTransformParameterfvHP = platform.createExtensionFunction( 
'glImageTransformParameterfvHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glImageTransformParameterfvHP(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetImageTransformParameterivHP = platform.createExtensionFunction( 
'glGetImageTransformParameterivHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetImageTransformParameterivHP(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetImageTransformParameterfvHP = platform.createExtensionFunction( 
'glGetImageTransformParameterfvHP',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glGetImageTransformParameterfvHP(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)


def glInitImageTransformHP():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
