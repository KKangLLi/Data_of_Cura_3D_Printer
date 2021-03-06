'''OpenGL extension SGIX.pixel_tiles

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_pixel_tiles'
_DEPRECATED = False
GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX = constant.Constant( 'GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX', 0x813E )
GL_PIXEL_TILE_CACHE_INCREMENT_SGIX = constant.Constant( 'GL_PIXEL_TILE_CACHE_INCREMENT_SGIX', 0x813F )
GL_PIXEL_TILE_WIDTH_SGIX = constant.Constant( 'GL_PIXEL_TILE_WIDTH_SGIX', 0x8140 )
GL_PIXEL_TILE_HEIGHT_SGIX = constant.Constant( 'GL_PIXEL_TILE_HEIGHT_SGIX', 0x8141 )
GL_PIXEL_TILE_GRID_WIDTH_SGIX = constant.Constant( 'GL_PIXEL_TILE_GRID_WIDTH_SGIX', 0x8142 )
GL_PIXEL_TILE_GRID_HEIGHT_SGIX = constant.Constant( 'GL_PIXEL_TILE_GRID_HEIGHT_SGIX', 0x8143 )
GL_PIXEL_TILE_GRID_DEPTH_SGIX = constant.Constant( 'GL_PIXEL_TILE_GRID_DEPTH_SGIX', 0x8144 )
GL_PIXEL_TILE_CACHE_SIZE_SGIX = constant.Constant( 'GL_PIXEL_TILE_CACHE_SIZE_SGIX', 0x8145 )


def glInitPixelTilesSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
