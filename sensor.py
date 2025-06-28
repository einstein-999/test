from __future__ import annotations
from typing import List, Tuple, Union, Any, Optional
import image
"""
<h3>sensor - BINARY</h3><p>BINARY (bitmap) pixel format. Each pixel is 1-bit.</p><p>This format is usful for mask storage. Can be used with <code>Image()</code> and <code>sensor.alloc_extra_fb()</code>.</p>
"""
BINARY: int = None
"""
<h3>sensor - GRAYSCALE</h3><p>GRAYSCALE pixel format (Y from YUV422). Each pixel is 8-bits, 1-byte.</p><p>All of our computer vision algorithms run faster on grayscale images than RGB565 images.</p>
"""
GRAYSCALE: int = None
"""
<h3>sensor - RGB565</h3><p>RGB565 pixel format. Each pixel is 16-bits, 2-bytes. 5-bits are used for red, 6-bits are used for green, and 5-bits are used for blue.</p><p>All of our computer vision algorithms run slower on RGB565 images than grayscale images.</p>
"""
RGB565: int = None
"""
<h3>sensor - BAYER</h3><p>RAW BAYER image pixel format. If you try to make the frame size too big to fit in the frame buffer your OpenMV Cam will set the pixel format to BAYER so that you can capture images but only some image processing methods will be operational.</p>
"""
BAYER: int = None
"""
<h3>sensor - YUV422</h3><p>A pixel format that is very easy to jpeg compress. Each pixel is stored as a grayscale 8-bit Y value followed by alternating 8-bit U/V color values that are shared between two Y values (8-bits Y1, 8-bits U, 8-bits Y2, 8-bits V, etc.). Only some image processing methods work with YUV422.</p>
"""
YUV422: int = None
"""
<h3>sensor - JPEG</h3><p>JPEG mode. The camera module outputs compressed jpeg images. Use <code>sensor.set_quality()</code> to control the jpeg quality. Only works for the OV2640/OV5640 cameras.</p>
"""
JPEG: int = None
"""
<h3>sensor - OV2640</h3><p><code>sensor.get_id()</code> returns this for the OV2640 camera.</p>
"""
OV2640: int = None
"""
<h3>sensor - OV5640</h3><p><code>sensor.get_id()</code> returns this for the OV5640 camera.</p>
"""
OV5640: int = None
"""
<h3>sensor - OV7690</h3><p><code>sensor.get_id()</code> returns this for the OV7690 camera.</p>
"""
OV7690: int = None
"""
<h3>sensor - OV7725</h3><p><code>sensor.get_id()</code> returns this for the OV7725 camera.</p>
"""
OV7725: int = None
"""
<h3>sensor - OV9650</h3><p><code>sensor.get_id()</code> returns this for the OV9650 camera.</p>
"""
OV9650: int = None
"""
<h3>sensor - MT9V022</h3><p><code>sensor.get_id()</code> returns this for the MT9V022 camera.</p>
"""
MT9V022: int = None
"""
<h3>sensor - MT9V024</h3><p><code>sensor.get_id()</code> returns this for the MT9V024 camera.</p>
"""
MT9V024: int = None
"""
<h3>sensor - MT9V032</h3><p><code>sensor.get_id()</code> returns this for the MT9V032 camera.</p>
"""
MT9V032: int = None
"""
<h3>sensor - MT9V034</h3><p><code>sensor.get_id()</code> returns this for the MT9V034 camera.</p>
"""
MT9V034: int = None
"""
<h3>sensor - MT9M114</h3><p><code>sensor.get_id()</code> returns this for the MT9M114 camera.</p>
"""
MT9M114: int = None
"""
<h3>sensor - BOSON320</h3><p><code>sensor.get_id()</code> returns this for the BOSON 320x256 camera.</p>
"""
BOSON320: int = None
"""
<h3>sensor - BOSON640</h3><p><code>sensor.get_id()</code> returns this for the BOSON 640x512 camera.</p>
"""
BOSON640: int = None
"""
<h3>sensor - LEPTON</h3><p><code>sensor.get_id()</code> returns this for the LEPTON1/2/3 cameras.</p>
"""
LEPTON: int = None
"""
<h3>sensor - HM01B0</h3><p><code>sensor.get_id()</code> returns this for the HM01B0 camera.</p>
"""
HM01B0: int = None
"""
<h3>sensor - HM0360</h3><p><code>sensor.get_id()</code> returns this for the HM0360 camera.</p>
"""
HM0360: int = None
"""
<h3>sensor - GC2145</h3><p><code>sensor.get_id()</code> returns this for the GC2145 camera.</p>
"""
GC2145: int = None
"""
<h3>sensor - GENX320ES</h3><p><code>sensor.get_id()</code> returns this for the GENX320 (Engineering Samples) camera.</p>
"""
GENX320ES: int = None
"""
<h3>sensor - GENX320</h3><p><code>sensor.get_id()</code> returns this for the GENX320 camera.</p>
"""
GENX320: int = None
"""
<h3>sensor - PAG7920</h3><p><code>sensor.get_id()</code> returns this for the PAG7920 camera.</p>
"""
PAG7920: int = None
"""
<h3>sensor - PAG7936</h3><p><code>sensor.get_id()</code> returns this for the PAG7936 camera.</p>
"""
PAG7936: int = None
"""
<h3>sensor - PAJ6100</h3><p><code>sensor.get_id()</code> returns this for the PAJ6100 camera.</p>
"""
PAJ6100: int = None
"""
<h3>sensor - FROGEYE2020</h3><p><code>sensor.get_id()</code> returns this for the FROGEYE2020 camera.</p>
"""
FROGEYE2020: int = None
"""
<h3>sensor - QQCIF</h3><p>88x72 resolution for the camera sensor.</p>
"""
QQCIF: int = None
"""
<h3>sensor - QCIF</h3><p>176x144 resolution for the camera sensor.</p>
"""
QCIF: int = None
"""
<h3>sensor - CIF</h3><p>352x288 resolution for the camera sensor.</p>
"""
CIF: int = None
"""
<h3>sensor - QQSIF</h3><p>88x60 resolution for the camera sensor.</p>
"""
QQSIF: int = None
"""
<h3>sensor - QSIF</h3><p>176x120 resolution for the camera sensor.</p>
"""
QSIF: int = None
"""
<h3>sensor - SIF</h3><p>352x240 resolution for the camera sensor.</p>
"""
SIF: int = None
"""
<h3>sensor - QQQQVGA</h3><p>40x30 resolution for the camera sensor.</p>
"""
QQQQVGA: int = None
"""
<h3>sensor - QQQVGA</h3><p>80x60 resolution for the camera sensor.</p>
"""
QQQVGA: int = None
"""
<h3>sensor - QQVGA</h3><p>160x120 resolution for the camera sensor.</p>
"""
QQVGA: int = None
"""
<h3>sensor - QVGA</h3><p>320x240 resolution for the camera sensor.</p>
"""
QVGA: int = None
"""
<h3>sensor - VGA</h3><p>640x480 resolution for the camera sensor.</p>
"""
VGA: int = None
"""
<h3>sensor - HQQQQVGA</h3><p>30x20 resolution for the camera sensor.</p>
"""
HQQQQVGA: int = None
"""
<h3>sensor - HQQQVGA</h3><p>60x40 resolution for the camera sensor.</p>
"""
HQQQVGA: int = None
"""
<h3>sensor - HQQVGA</h3><p>120x80 resolution for the camera sensor.</p>
"""
HQQVGA: int = None
"""
<h3>sensor - HQVGA</h3><p>240x160 resolution for the camera sensor.</p>
"""
HQVGA: int = None
"""
<h3>sensor - HVGA</h3><p>480x320 resolution for the camera sensor.</p>
"""
HVGA: int = None
"""
<h3>sensor - B64X32</h3><p>64x32 resolution for the camera sensor.</p><p>For use with <code>Image.find_displacement()</code> and any other FFT based algorithm.</p>
"""
B64X32: int = None
"""
<h3>sensor - B64X64</h3><p>64x64 resolution for the camera sensor.</p><p>For use with <code>Image.find_displacement()</code> and any other FFT based algorithm.</p>
"""
B64X64: int = None
"""
<h3>sensor - B128X64</h3><p>128x64 resolution for the camera sensor.</p><p>For use with <code>Image.find_displacement()</code> and any other FFT based algorithm.</p>
"""
B128X64: int = None
"""
<h3>sensor - B128X128</h3><p>128x128 resolution for the camera sensor.</p><p>For use with <code>Image.find_displacement()</code> and any other FFT based algorithm.</p>
"""
B128X128: int = None
"""
<h3>sensor - B160X160</h3><p>160x160 resolution for the HM01B0 camera sensor.</p>
"""
B160X160: int = None
"""
<h3>sensor - B320X320</h3><p>320x320 resolution for the HM01B0 camera sensor.</p>
"""
B320X320: int = None
"""
<h3>sensor - LCD</h3><p>128x160 resolution for the camera sensor (for use with the lcd shield).</p>
"""
LCD: int = None
"""
<h3>sensor - QQVGA2</h3><p>128x160 resolution for the camera sensor (for use with the lcd shield).</p>
"""
QQVGA2: int = None
"""
<h3>sensor - WVGA</h3><p>720x480 resolution for the MT9V034 camera sensor.</p>
"""
WVGA: int = None
"""
<h3>sensor - WVGA2</h3><p>752x480 resolution for the MT9V034 camera sensor.</p>
"""
WVGA2: int = None
"""
<h3>sensor - SVGA</h3><p>800x600 resolution for the camera sensor.</p>
"""
SVGA: int = None
"""
<h3>sensor - XGA</h3><p>1024x768 resolution for the camera sensor.</p>
"""
XGA: int = None
"""
<h3>sensor - WXGA</h3><p>1280x768 resolution for the MT9M114 camera sensor.</p>
"""
WXGA: int = None
"""
<h3>sensor - SXGA</h3><p>1280x1024 resolution for the camera sensor. Only works for the OV2640/OV5640 cameras.</p>
"""
SXGA: int = None
"""
<h3>sensor - SXGAM</h3><p>1280x960 resolution for the MT9M114 camera sensor.</p>
"""
SXGAM: int = None
"""
<h3>sensor - UXGA</h3><p>1600x1200 resolution for the camera sensor. Only works for the OV2640/OV5640 cameras.</p>
"""
UXGA: int = None
"""
<h3>sensor - HD</h3><p>1280x720 resolution for the camera sensor.</p>
"""
HD: int = None
"""
<h3>sensor - FHD</h3><p>1920x1080 resolution for the camera sensor. Only works for the OV5640 camera.</p>
"""
FHD: int = None
"""
<h3>sensor - QHD</h3><p>2560x1440 resolution for the camera sensor. Only works for the OV5640 camera.</p>
"""
QHD: int = None
"""
<h3>sensor - QXGA</h3><p>2048x1536 resolution for the camera sensor. Only works for the OV5640 camera.</p>
"""
QXGA: int = None
"""
<h3>sensor - WQXGA</h3><p>2560x1600 resolution for the camera sensor. Only works for the OV5640 camera.</p>
"""
WQXGA: int = None
"""
<h3>sensor - WQXGA2</h3><p>2592x1944 resolution for the camera sensor. Only works for the OV5640 camera.</p>
"""
WQXGA2: int = None
"""
<h3>sensor - IOCTL_SET_READOUT_WINDOW</h3><p>Lets you set the readout window for the OV5640.</p>
"""
IOCTL_SET_READOUT_WINDOW: int = None
"""
<h3>sensor - IOCTL_GET_READOUT_WINDOW</h3><p>Lets you get the readout window for the OV5640.</p>
"""
IOCTL_GET_READOUT_WINDOW: int = None
"""
<h3>sensor - IOCTL_SET_TRIGGERED_MODE</h3><p>Lets you set the triggered mode for the MT9V034.</p>
"""
IOCTL_SET_TRIGGERED_MODE: int = None
"""
<h3>sensor - IOCTL_GET_TRIGGERED_MODE</h3><p>Lets you get the triggered mode for the MT9V034.</p>
"""
IOCTL_GET_TRIGGERED_MODE: int = None
"""
<h3>sensor - IOCTL_SET_FOV_WIDE</h3><p>Enable <code>sensor.set_framesize()</code> to optimize for the field-of-view over FPS.</p>
"""
IOCTL_SET_FOV_WIDE: int = None
"""
<h3>sensor - IOCTL_GET_FOV_WIDE</h3><p>Return if <code>sensor.set_framesize()</code> is optimizing for field-of-view over FPS.</p>
"""
IOCTL_GET_FOV_WIDE: int = None
"""
<h3>sensor - IOCTL_TRIGGER_AUTO_FOCUS</h3><p>Used to trigger auto focus for the OV5640 FPC camera module.</p>
"""
IOCTL_TRIGGER_AUTO_FOCUS: int = None
"""
<h3>sensor - IOCTL_PAUSE_AUTO_FOCUS</h3><p>Used to pause auto focus (while running) for the OV5640 FPC camera module.</p>
"""
IOCTL_PAUSE_AUTO_FOCUS: int = None
"""
<h3>sensor - IOCTL_RESET_AUTO_FOCUS</h3><p>Used to reset auto focus back to the default for the OV5640 FPC camera module.</p>
"""
IOCTL_RESET_AUTO_FOCUS: int = None
"""
<h3>sensor - IOCTL_WAIT_ON_AUTO_FOCUS</h3><p>Used to wait on auto focus to finish after being triggered for the OV5640 FPC camera module.</p>
"""
IOCTL_WAIT_ON_AUTO_FOCUS: int = None
"""
<h3>sensor - IOCTL_SET_NIGHT_MODE</h3><p>Used to turn night mode on or off on a sensor. Nightmode reduces the frame rate to increase exposure dynamically.</p>
"""
IOCTL_SET_NIGHT_MODE: int = None
"""
<h3>sensor - IOCTL_GET_NIGHT_MODE</h3><p>Gets the current value of if night mode is enabled or disabled for your sensor.</p>
"""
IOCTL_GET_NIGHT_MODE: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_WIDTH</h3><p>Lets you get the FLIR Lepton image resolution width in pixels.</p>
"""
IOCTL_LEPTON_GET_WIDTH: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_HEIGHT</h3><p>Lets you get the FLIR Lepton image resolution height in pixels.</p>
"""
IOCTL_LEPTON_GET_HEIGHT: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_RADIOMETRY</h3><p>Lets you get the FLIR Lepton type (radiometric or not).</p>
"""
IOCTL_LEPTON_GET_RADIOMETRY: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_REFRESH</h3><p>Lets you get the FLIR Lepton refresh rate in hertz.</p>
"""
IOCTL_LEPTON_GET_REFRESH: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_RESOLUTION</h3><p>Lets you get the FLIR Lepton ADC resolution in bits.</p>
"""
IOCTL_LEPTON_GET_RESOLUTION: int = None
"""
<h3>sensor - IOCTL_LEPTON_RUN_COMMAND</h3><p>Executes a 16-bit command given the FLIR Lepton SDK.</p>
"""
IOCTL_LEPTON_RUN_COMMAND: int = None
"""
<h3>sensor - IOCTL_LEPTON_SET_ATTRIBUTE</h3><p>Sets a FLIR Lepton Attribute given the FLIR Lepton SDK.</p>
"""
IOCTL_LEPTON_SET_ATTRIBUTE: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_ATTRIBUTE</h3><p>Gets a FLIR Lepton Attribute given the FLIR Lepton SDK.</p>
"""
IOCTL_LEPTON_GET_ATTRIBUTE: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_FPA_TEMP</h3><p>Gets the FLIR Lepton FPA temp in celsius.</p>
"""
IOCTL_LEPTON_GET_FPA_TEMP: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_AUX_TEMP</h3><p>Gets the FLIR Lepton AUX temp in celsius.</p>
"""
IOCTL_LEPTON_GET_AUX_TEMP: int = None
"""
<h3>sensor - IOCTL_LEPTON_SET_MODE</h3><p>Lets you set the FLIR Lepton driver into a mode where you can get a valid temperature value per pixel. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_LEPTON_SET_MODE: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_MODE</h3><p>Lets you get if measurement mode is enabled or not for the FLIR Lepton sensor. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_LEPTON_GET_MODE: int = None
"""
<h3>sensor - IOCTL_LEPTON_SET_RANGE</h3><p>Lets you set the temperature range you want to map pixels in the image to when in measurement mode. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_LEPTON_SET_RANGE: int = None
"""
<h3>sensor - IOCTL_LEPTON_GET_RANGE</h3><p>Lets you get the temperature range used for measurement mode. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_LEPTON_GET_RANGE: int = None
"""
<h3>sensor - IOCTL_HIMAX_MD_ENABLE</h3><p>Lets you control the motion detection interrupt on the HM01B0. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_HIMAX_MD_ENABLE: int = None
"""
<h3>sensor - IOCTL_HIMAX_MD_CLEAR</h3><p>Lets you control the motion detection interrupt on the HM01B0. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_HIMAX_MD_CLEAR: int = None
"""
<h3>sensor - IOCTL_HIMAX_MD_WINDOW</h3><p>Lets you control the motion detection interrupt on the HM01B0. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_HIMAX_MD_WINDOW: int = None
"""
<h3>sensor - IOCTL_HIMAX_MD_THRESHOLD</h3><p>Lets you control the motion detection interrupt on the HM01B0. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_HIMAX_MD_THRESHOLD: int = None
"""
<h3>sensor - IOCTL_HIMAX_OSC_ENABLE</h3><p>Lets you control the internal oscillator on the HM01B0. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_HIMAX_OSC_ENABLE: int = None
"""
<h3>sensor - IOCTL_RGB_STATS</h3><p>Lets you get the RGB statistics from the camera sensor. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_RGB_STATS: int = None
"""
<h3>sensor - IOCTL_GENX320_SET_BIASES</h3><p>Lets you set the GENX320 camera sensor biases. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_GENX320_SET_BIASES: int = None
"""
<h3>sensor - GENX320_BIASES_DEFAULT</h3><p>Default biases for the GENX320 camera sensor.</p>
"""
GENX320_BIASES_DEFAULT: int = None
"""
<h3>sensor - GENX320_BIASES_LOW_LIGHT</h3><p>Low light biases for the GENX320 camera sensor.</p>
"""
GENX320_BIASES_LOW_LIGHT: int = None
"""
<h3>sensor - GENX320_BIASES_ACTIVE_MARKER</h3><p>Active marker biases for the GENX320 camera sensor.</p>
"""
GENX320_BIASES_ACTIVE_MARKER: int = None
"""
<h3>sensor - GENX320_BIASES_LOW_NOISE</h3><p>Low noise biases for the GENX320 camera sensor.</p>
"""
GENX320_BIASES_LOW_NOISE: int = None
"""
<h3>sensor - GENX320_BIASES_HIGH_SPEED</h3><p>High speed biases for the GENX320 camera sensor.</p>
"""
GENX320_BIASES_HIGH_SPEED: int = None
"""
<h3>sensor - IOCTL_GENX320_SET_BIAS</h3><p>Lets you set a single GENX320 camera sensor bias. See <code>sensor.ioctl()</code> for more information.</p>
"""
IOCTL_GENX320_SET_BIAS: int = None
"""
<h3>sensor - GENX320_BIAS_DIFF_OFF</h3><p>Set the GENX320 DIFF OFF bias.</p>
"""
GENX320_BIAS_DIFF_OFF: int = None
"""
<h3>sensor - GENX320_BIAS_DIFF_ON</h3><p>Set the GENX320 DIFF ON bias.</p>
"""
GENX320_BIAS_DIFF_ON: int = None
"""
<h3>sensor - GENX320_BIAS_FO</h3><p>Set the GENX320 FO bias.</p>
"""
GENX320_BIAS_FO: int = None
"""
<h3>sensor - GENX320_BIAS_HPF</h3><p>Set the GENX320 HPF bias.</p>
"""
GENX320_BIAS_HPF: int = None
"""
<h3>sensor - ENX320_BIAS_REFR</h3><p>Set the GENX320 REFR bias.</p>
"""
ENX320_BIAS_REFR: int = None
"""
<h3>sensor - SINGLE_BUFFER</h3><p>Pass to <code>sensor.set_framebuffers()</code> to set single buffer mode (1 buffer).</p>
"""
SINGLE_BUFFER: int = None
"""
<h3>sensor - DOUBLE_BUFFER</h3><p>Pass to <code>sensor.set_framebuffers()</code> to set double buffer mode (2 buffers).</p>
"""
DOUBLE_BUFFER: int = None
"""
<h3>sensor - TRIPLE_BUFFER</h3><p>Pass to <code>sensor.set_framebuffers()</code> to set triple buffer mode (3 buffers).</p>
"""
TRIPLE_BUFFER: int = None
"""
<h3>sensor - VIDEO_FIFO</h3><p>Pass to <code>sensor.set_framebuffers()</code> to set video FIFO mode (4 buffers).</p>
"""
VIDEO_FIFO: int = None
def reset() -> None:
    """
    <h3>sensor - reset()</h3><p>Initializes the camera sensor.</p>
    """
    pass
def sleep(enable:bool) -> None:
    """
    <h3>sensor - sleep(enable: bool)</h3><p>Puts the camera to sleep if enable is True. Otherwise, wakes it back up.</p>
    """
    pass
def shutdown(enable:bool) -> None:
    """
    <h3>sensor - shutdown(enable: bool)</h3><p>Puts the camera into a lower power mode than sleep (but the camera must be reset on being woken up).</p>
    """
    pass
def flush() -> None:
    """
    <h3>sensor - flush()</h3><p>Copies whatever was in the frame buffer to the IDE. You should call this method to display the last image your OpenMV Cam takes if it’s not running a script with an infinite loop. Note that you’ll need to add a delay time of about a second after your script finishes for the IDE to grab the image from your camera. Otherwise, this method will have no effect.</p>
    """
    pass
def snapshot() -> image.Image:
    """
    <h3>sensor - snapshot()</h3><p>Takes a picture using the camera and returns an <code>image</code> object.</p><p>The OpenMV Cam has two memory areas for images. The classical stack/heap area used for normal MicroPython processing can store small images within it’s heap. However, the MicroPython heap is only about ~100 KB which is not enough to store larger images. So, your OpenMV Cam has a secondary frame buffer memory area that stores images taken by <code>sensor.snapshot()</code>. Images are stored on the bottom of this memory area. Any memory that’s left over is then available for use by the frame buffer stack which your OpenMV Cam’s firmware uses to hold large temporary data structures for image processing algorithms.</p><p>If you need room to hold multiple frames you may “steal” frame buffer space by calling <code>sensor.alloc_extra_fb()</code>.</p><p>If <code>sensor.set_auto_rotation()</code> is enabled this method will return a new already rotated <code>image</code> object.</p><div><p>Note</p><p><code>sensor.snapshot()</code> may apply cropping parameters to fit the snapshot in the available RAM the pixformat, framesize, windowing, and framebuffers. The cropping parameters will be applied to maintain the aspect ratio and will stay until <code>sensor.set_framesize()</code> or <code>sensor.set_windowing()</code> are called.</p></div>
    """
    pass
def skip_frames(n:int|None=None, time:int|None=None) -> None:
    """
    <h3>sensor - skip_frames(n: int | None = None, time: int | None = None)</h3><p>Takes <code>n</code> number of snapshots to let the camera image stabilize after changing camera settings. <code>n</code> is passed as normal argument, e.g. <code>skip_frames(10)</code> to skip 10 frames. You should call this function after changing camera settings.</p><p>Alternatively, you can pass the keyword argument <code>time</code> to skip frames for some number of milliseconds, e.g. <code>skip_frames(time = 2000)</code> to skip frames for 2000 milliseconds.</p><p>If neither <code>n</code> nor <code>time</code> is specified this method skips frames for 300 milliseconds.</p><p>If both are specified this method skips <code>n</code> number of frames but will timeout after <code>time</code> milliseconds.</p><div><p>Note</p><p><code>sensor.snapshot()</code> may apply cropping parameters to fit the snapshot in the available RAM given the pixformat, framesize, windowing, and framebuffers. The cropping parameters will be applied to maintain the aspect ratio and will stay until <code>sensor.set_framesize()</code> or <code>sensor.set_windowing()</code> are called.</p></div>
    """
    pass
def width() -> int:
    """
    <h3>sensor - width()</h3><p>Returns the sensor resolution width.</p>
    """
    pass
def height() -> int:
    """
    <h3>sensor - height()</h3><p>Returns the sensor resolution height.</p>
    """
    pass
def get_fb() -> image.Image|None:
    """
    <h3>sensor - get_fb()</h3><p>(Get Frame Buffer) Returns the image object returned by a previous call of <code>sensor.snapshot()</code>. If <code>sensor.snapshot()</code> had not been called before then <code>None</code> is returned.</p>
    """
    pass
def get_id() -> int:
    """
    <h3>sensor - get_id()</h3><p>Returns the camera module ID.</p><div><ul><li><code>sensor.OV2640</code>: Second gen OpenMV Cam sensor - never released.</li><li><code>sensor.OV5640</code>: High-res OpenMV Cam H7 Plus sensor.</li><li><code>sensor.OV7690</code>: OpenMV Cam Micro sensor module.</li><li><code>sensor.OV7725</code>: Rolling shutter sensor module.</li><li><code>sensor.OV9650</code>: First gen OpenMV Cam sensor - never released.</li><li><code>sensor.MT9V022</code>: Global shutter sensor module.</li><li><code>sensor.MT9V024</code>: Global shutter sensor module.</li><li><code>sensor.MT9V032</code>: Global shutter sensor module.</li><li><code>sensor.MT9V034</code>: Global shutter sensor module.</li><li><code>sensor.MT9M114</code>: OV7725 replacement rolling shutter sensor module.</li><li><code>sensor.BOSON320</code>: Boson 320x256 thermal sensor module.</li><li><code>sensor.BOSON640</code>: Boson 640x512 thermal sensor module.</li><li><code>sensor.LEPTON</code>: Lepton1/2/3 sensor module.</li><li><code>sensor.HM01B0</code>: Arduino Portenta H7 sensor module.</li><li><code>sensor.HM0360</code>: Arduino Portenta H7 sensor module.</li><li><code>sensor.GC2145</code>: Arduino Nicla Vision H7 sensor module.</li><li><code>sensor.GENX320ES</code>: Prophesee Event Camera sensor module (engineering sample).</li><li><code>sensor.GENX320</code>: Prophesee Event Camera sensor module.</li><li><code>sensor.PAG7920</code>: PixArt Imaging sensor Module.</li><li><code>sensor.PAG7936</code>: PixArt Imaging sensor Module.</li><li><code>sensor.PAJ6100</code>: PixArt Imaging sensor Module.</li><li><code>sensor.FROGEYE2020</code> : FrogEye2020 event camera sensor module - never released.</li></ul></div>
    """
    pass
def alloc_extra_fb(width:int, height:int, pixformat:int) -> image.Image:
    """
    <h3>sensor - alloc_extra_fb(width: int, height: int, pixformat: int)</h3><p>Allocates another frame buffer for image storage from the frame buffer stack and returns an <code>image</code> object of <code>width</code>, <code>height</code>, and <code>pixformat</code>.</p><p>You may call this function as many times as you like as long as there’s memory available to allocate any number of extra frame buffers.</p><p>If <code>pixformat</code> is a number &gt;= 4 then this will allocate a JPEG image. You can then do <code>Image.bytearray()</code> to get byte level read/write access to the JPEG image.</p><div><p>Note</p><p>Creating secondary images normally requires creating them on the heap which has a limited amount of RAM… but, also gets fragmented making it hard to grab a large contigous memory array to store an image in. With this method you are able to allocate a very large memory array for an image instantly by taking space away from our frame buffer stack memory which we use for computer vision algorithms. That said, this also means you’ll run out of memory more easily if you try to execute more memory intensive machine vision algorithms like <code>Image.find_apriltags()</code>.</p></div>
    """
    pass
def dealloc_extra_fb() -> None:
    """
    <h3>sensor - dealloc_extra_fb()</h3><p>Deallocates the last previously allocated extra frame buffer. Extra frame buffers are stored in a stack like structure.</p><div><p>Note</p><p>Your OpenMV Cam has two memory areas. First, you have your classical .data/.bss/heap/stack memory area. The .data/.bss/heap regions are fixed by firmware. The stack then grows down until it hits the heap. Next, frame buffers are stored in a secondary memory region. Memory is liad out with the main frame buffer on the bottom and the frame buffer stack on the top. When <code>sensor.snapshot()</code> is called it fills the frame bufer from the bottom. The frame buffer stack is then able to use whatever is left over. This memory allocation method is extremely efficent for computer vision on microcontrollers.</p></div>
    """
    pass
def set_pixformat(pixformat:int) -> None:
    """
    <h3>sensor - set_pixformat(pixformat: int)</h3><p>Sets the pixel format for the camera module.</p><div><ul><li><code>sensor.GRAYSCALE</code>: 8-bits per pixel.</li><li><code>sensor.RGB565</code>: 16-bits per pixel.</li><li><code>sensor.BAYER</code>: 8-bits per pixel bayer pattern.</li><li><code>sensor.YUV422</code>: 16-bits per pixel (8-bits Y1, 8-bits U, 8-bits Y2, 8-bits V, etc.)</li><li><code>sensor.JPEG</code>: Compressed JPEG data. Only for the OV2640/OV5640.</li></ul></div><p>If you are trying to take JPEG images with the OV2640 or OV5640 camera modules at high resolutions you should set the pixformat to <code>sensor.JPEG</code>. You can control the image quality then with <code>sensor.set_quality()</code>.</p>
    """
    pass
def get_pixformat() -> int:
    """
    <h3>sensor - get_pixformat()</h3><p>Returns the pixformat for the camera module.</p>
    """
    pass
def set_framesize(framesize:int) -> None:
    """
    <h3>sensor - set_framesize(framesize: int)</h3><p>Sets the frame size for the camera module.</p><div><ul><li><code>sensor.QQCIF</code>: 88x72</li><li><code>sensor.QCIF</code>: 176x144</li><li><code>sensor.CIF</code>: 352x288</li><li><code>sensor.QQSIF</code>: 88x60</li><li><code>sensor.QSIF</code>: 176x120</li><li><code>sensor.SIF</code>: 352x240</li><li><code>sensor.QQQQVGA</code>: 40x30</li><li><code>sensor.QQQVGA</code>: 80x60</li><li><code>sensor.QQVGA</code>: 160x120</li><li><code>sensor.QVGA</code>: 320x240</li><li><code>sensor.VGA</code>: 640x480</li><li><code>sensor.HQQQQVGA</code>: 30x20</li><li><code>sensor.HQQQVGA</code>: 60x40</li><li><code>sensor.HQQVGA</code>: 120x80</li><li><code>sensor.HQVGA</code>: 240x160</li><li><code>sensor.HVGA</code>: 480x320</li><li><code>sensor.B64X32</code>: 64x32 (for use with <code>Image.find_displacement()</code>)</li><li><code>sensor.B64X64</code>: 64x64 (for use with <code>Image.find_displacement()</code>)</li><li><code>sensor.B128X64</code>: 128x64 (for use with <code>Image.find_displacement()</code>)</li><li><code>sensor.B128X128</code>: 128x128 (for use with <code>Image.find_displacement()</code>)</li><li><code>sensor.B160X160</code>: 160x160 (for the HM01B0)</li><li><code>sensor.B320X320</code>: 320x320 (for the HM01B0)</li><li><code>sensor.LCD</code>: 128x160 (for use with the lcd shield)</li><li><code>sensor.QQVGA2</code>: 128x160 (for use with the lcd shield)</li><li><code>sensor.WVGA</code>: 720x480 (for the MT9V034)</li><li><code>sensor.WVGA2</code>:752x480 (for the MT9V034)</li><li><code>sensor.SVGA</code>: 800x600 (only for the OV2640/OV5640 sensor)</li><li><code>sensor.XGA</code>: 1024x768 (only for the OV2640/OV5640 sensor)</li><li><code>sensor.WXGA</code>: 1280x768 (for the MT9M114)</li><li><code>sensor.SXGA</code>: 1280x1024 (only for the OV2640/OV5640 sensor)</li><li><code>sensor.SXGAM</code>: 1280x960 (for the MT9M114)</li><li><code>sensor.UXGA</code>: 1600x1200 (only for the OV2640/OV5640 sensor)</li><li><code>sensor.HD</code>: 1280x720 (only for the OV2640/OV5640 sensor)</li><li><code>sensor.FHD</code>: 1920x1080 (only for the OV5640 sensor)</li><li><code>sensor.QHD</code>: 2560x1440 (only for the OV5640 sensor)</li><li><code>sensor.QXGA</code>: 2048x1536 (only for the OV5640 sensor)</li><li><code>sensor.WQXGA</code>: 2560x1600 (only for the OV5640 sensor)</li><li><code>sensor.WQXGA2</code>: 2592x1944 (only for the OV5640 sensor)</li></ul></div>
    """
    pass
def get_framesize() -> int:
    """
    <h3>sensor - get_framesize()</h3><p>Returns the frame size for the camera module.</p>
    """
    pass
def set_framerate(rate:int) -> None:
    """
    <h3>sensor - set_framerate(rate: int)</h3><p>Sets the frame rate in hz for the camera module.</p><div><p>Note</p><p><code>set_framerate</code> works by dropping frames received by the camera module to keep the frame rate equal to (or below) the rate you specify. By default the camera will run at the maximum frame rate. If implemented for the particular camera sensor then <code>set_framerate</code> will also reduce the camera sensor frame rate internally to save power and improve image quality by increasing the sensor exposure. <code>set_framerate</code> may conflict with <code>set_auto_exposure</code> on some cameras.</p></div>
    """
    pass
def get_framerate() -> int:
    """
    <h3>sensor - get_framerate()</h3><p>Returns the frame rate in hz for the camera module.</p>
    """
    pass
def set_windowing(roi:Tuple[int,int]|Tuple[int,int,int,int]) -> None:
    """
    <h3>sensor - set_windowing(roi: Tuple[int, int] | Tuple[int, int, int, int])</h3><p>Sets the resolution of the camera to a sub resolution inside of the current resolution. For example, setting the resolution to <code>sensor.VGA</code> and then the windowing to (120, 140, 200, 200) sets <code>sensor.snapshot()</code> to capture the 200x200 center pixels of the VGA resolution outputted by the camera sensor. You can use windowing to get custom resolutions. Also, when using windowing on a larger resolution you effectively are digital zooming.</p><p><code>roi</code> is a rect tuple (x, y, w, h). However, you may just pass (w, h) and the <code>roi</code> will be centered on the frame. You may also pass roi not in parens.</p><p>This function will automatically handle cropping the passed roi to the framesize.</p>
    """
    pass
def get_windowing() -> Tuple[int,int,int,int]:
    """
    <h3>sensor - get_windowing()</h3><p>Returns the <code>roi</code> tuple (x, y, w, h) previously set with <code>sensor.set_windowing()</code>.</p>
    """
    pass
def set_gainceiling(gainceiling:int) -> None:
    """
    <h3>sensor - set_gainceiling(gainceiling: int)</h3><p>Set the camera image gainceiling. 2, 4, 8, 16, 32, 64, or 128.</p>
    """
    pass
def set_contrast(constrast:int) -> None:
    """
    <h3>sensor - set_contrast(constrast: int)</h3><p>Set the camera image contrast. -3 to +3.</p>
    """
    pass
def set_brightness(brightness:int) -> None:
    """
    <h3>sensor - set_brightness(brightness: int)</h3><p>Set the camera image brightness. -3 to +3.</p>
    """
    pass
def set_saturation(saturation:int) -> None:
    """
    <h3>sensor - set_saturation(saturation: int)</h3><p>Set the camera image saturation. -3 to +3.</p>
    """
    pass
def set_quality(quality:int) -> None:
    """
    <h3>sensor - set_quality(quality: int)</h3><p>Set the camera image JPEG compression quality. 0 - 100.</p><div><p>Note</p><p>Only for the OV2640/OV5640 cameras.</p></div>
    """
    pass
def set_colorbar(enable:bool) -> None:
    """
    <h3>sensor - set_colorbar(enable: bool)</h3><p>Turns color bar mode on (True) or off (False). Defaults to off.</p>
    """
    pass
def set_auto_gain(enable:bool, gain_db=-1, gain_db_ceiling:int|None=None) -> None:
    """
    <h3>sensor - set_auto_gain(enable: bool, gain_db=-1, gain_db_ceiling: int | None = None)</h3><p><code>enable</code> turns auto gain control on (True) or off (False). The camera will startup with auto gain control on.</p><p>If <code>enable</code> is False you may set a fixed gain in decibels with <code>gain_db</code>.</p><p>If <code>enable</code> is True you may set the maximum gain ceiling in decibels with <code>gain_db_ceiling</code> for the automatic gain control algorithm.</p><div><p>Note</p><p>You need to turn off white balance too if you want to track colors.</p></div>
    """
    pass
def get_gain_db() -> float:
    """
    <h3>sensor - get_gain_db()</h3><p>Returns the current camera gain value in decibels (float).</p>
    """
    pass
def set_auto_exposure(enable:bool, exposure_us:int|None=None) -> None:
    """
    <h3>sensor - set_auto_exposure(enable: bool, exposure_us: int | None = None)</h3><p><code>enable</code> turns auto exposure control on (True) or off (False). The camera will startup with auto exposure control on.</p><p>If <code>enable</code> is False you may set a fixed exposure time in microseconds with <code>exposure_us</code>.</p><div><p>Note</p><p>Camera auto exposure algorithms are pretty conservative about how much they adjust the exposure value by and will generally avoid changing the exposure value by much. Instead, they change the gain value alot of deal with changing lighting.</p></div>
    """
    pass
def get_exposure_us() -> int:
    """
    <h3>sensor - get_exposure_us()</h3><p>Returns the current camera exposure value in microseconds (int).</p>
    """
    pass
def set_auto_whitebal(enable:bool, rgb_gain_db:Tuple[float,float,float]|None=None) -> None:
    """
    <h3>sensor - set_auto_whitebal(enable: bool, rgb_gain_db: Tuple[float, float, float] | None = None)</h3><p><code>enable</code> turns auto white balance on (True) or off (False). The camera will startup with auto white balance on.</p><p>If <code>enable</code> is False you may set a fixed gain in decibels for the red, green, and blue channels respectively with <code>rgb_gain_db</code>.</p><div><p>Note</p><p>You need to turn off gain control too if you want to track colors.</p></div>
    """
    pass
def get_rgb_gain_db() -> Tuple[float,float,float]:
    """
    <h3>sensor - get_rgb_gain_db()</h3><p>Returns a tuple with the current camera red, green, and blue gain values in decibels ((float, float, float)).</p>
    """
    pass
def set_auto_blc(enable:bool, regs:Any|None=None):
    """
    <h3>sensor - set_auto_blc(enable: bool, regs: Any | None = None)</h3><p>Sets the auto black line calibration (blc) control on the camera.</p><p><code>enable</code> pass <code>True</code> or <code>False</code> to turn BLC on or off. You typically always want this on.</p><p><code>regs</code> if disabled then you can manually set the blc register values via the values you got previously from <code>get_blc_regs()</code>.</p>
    """
    pass
def get_blc_regs() -> Any:
    """
    <h3>sensor - get_blc_regs()</h3><p>Returns the sensor blc registers as an opaque tuple of integers. For use with <code>set_auto_blc</code>.</p>
    """
    pass
def set_hmirror(enable:bool) -> None:
    """
    <h3>sensor - set_hmirror(enable: bool)</h3><p>Turns horizontal mirror mode on (True) or off (False). Defaults to off.</p>
    """
    pass
def get_hmirror() -> bool:
    """
    <h3>sensor - get_hmirror()</h3><p>Returns if horizontal mirror mode is enabled.</p>
    """
    pass
def set_vflip(enable:bool) -> None:
    """
    <h3>sensor - set_vflip(enable: bool)</h3><p>Turns vertical flip mode on (True) or off (False). Defaults to off.</p>
    """
    pass
def get_vflip() -> bool:
    """
    <h3>sensor - get_vflip()</h3><p>Returns if vertical flip mode is enabled.</p>
    """
    pass
def set_transpose(enable:bool) -> None:
    """
    <h3>sensor - set_transpose(enable: bool)</h3><p>Turns transpose mode on (True) or off (False). Defaults to off.</p><div><ul><li>vflip=False, hmirror=False, transpose=False -&gt; 0 degree rotation</li><li>vflip=True, hmirror=False, transpose=True -&gt; 90 degree rotation</li><li>vflip=True, hmirror=True, transpose=False -&gt; 180 degree rotation</li><li>vflip=False, hmirror=True, transpose=True -&gt; 270 degree rotation</li></ul></div>
    """
    pass
def get_transpose() -> bool:
    """
    <h3>sensor - get_transpose()</h3><p>Returns if transpose mode is enabled.</p>
    """
    pass
def set_auto_rotation(enable:bool) -> None:
    """
    <h3>sensor - set_auto_rotation(enable: bool)</h3><p>Turns auto rotation mode on (True) or off (False). Defaults to off.</p><div><p>Note</p><p>This function only works when the OpenMV Cam has an <code>imu</code> installed and is enabled automatically.</p></div>
    """
    pass
def get_auto_rotation() -> bool:
    """
    <h3>sensor - get_auto_rotation()</h3><p>Returns if auto rotation mode is enabled.</p><div><p>Note</p><p>This function only works when the OpenMV Cam has an <code>imu</code> installed and is enabled automatically.</p></div>
    """
    pass
def set_framebuffers(count:int) -> None:
    """
    <h3>sensor - set_framebuffers(count: int)</h3><p>Sets the number of frame buffers used to receive image data. By default your OpenMV Cam will automatically try to allocate the maximum number of frame buffers it can possibly allocate without using more than 1/2 of the available frame buffer RAM at the time of allocation to ensure the best performance. Automatic reallocation of frame buffers occurs whenever you call <code>sensor.set_pixformat()</code>, <code>sensor.set_framesize()</code>, and <code>sensor.set_windowing()</code>.</p><p><code>sensor.snapshot()</code> will automatically handle switching active frame buffers in the background. From your code’s perspective there is only ever 1 active frame buffer even though there might be more than 1 frame buffer on the system and another frame buffer reciving data in the background.</p><p>If count is:</p><div><dl><dt>1 - Single Buffer Mode (you may also pass <code>sensor.SINGLE_BUFFER</code>)</dt><dd><p>In single buffer mode your OpenMV Cam will allocate one frame buffer for receiving images. When you call <code>sensor.snapshot()</code> that framebuffer will be used to receive the image and the camera driver will continue to run. In the advent you call <code>sensor.snapshot()</code> again before the first line of the next frame is received your code will execute at the frame rate of the camera. Otherwise, the image will be dropped.</p></dd><dt>2 - Double Buffer Mode (you may also pass <code>sensor.DOUBLE_BUFFER</code>)</dt><dd><p>In double buffer mode your OpenMV Cam will allocate two frame buffers for receiving images. When you call <code>sensor.snapshot()</code> one framebuffer will be used to receive the image and the camera driver will continue to run. When the next frame is received it will be stored in the other frame bufer. In the advent you call <code>sensor.snapshot()</code> again before the first line of the next frame after is received your code will execute at the frame rate of the camera. Otherwise, the image will be dropped.</p></dd><dt>3 - Triple Buffer Mode (you may also pass <code>sensor.TRIPLE_BUFFER</code>)</dt><dd><p>In triple buffer mode your OpenMV Cam will allocate three buffers for receiving images. In this mode there is always a frame buffer to store the received image to in the background resulting in the highest performance and lowest latency for reading the latest received frame. No frames are ever dropped in this mode. The next frame read by <code>sensor.snapshot()</code> is the last captured frame by the sensor driver (e.g. if you are reading slower than the camera frame rate then the older frame in the possible frames available is skipped).</p>
    """
    pass
def get_framebuffers() -> int:
    """
    <h3>sensor - get_framebuffers()</h3><p>Returns the current number of frame buffers allocated.</p>
    """
    pass
def disable_delays(disable:bool|None=None) -> bool:
    """
    <h3>sensor - disable_delays(disable: bool | None = None)</h3><p>If <code>disable</code> is <code>True</code> then disable all settling time delays in the sensor module. Whenever you reset the camera module, change modes, etc. the sensor driver delays to prevent you can from calling <code>snapshot</code> to quickly afterwards and receiving corrupt frames from the camera module. By disabling delays you can quickly update the camera module settings in bulk via multiple function calls before delaying at the end and calling <code>snapshot</code>.</p><p>If this function is called with no arguments it returns if delays are disabled.</p>
    """
    pass
def disable_full_flush(disable:bool|None=None) -> bool:
    """
    <h3>sensor - disable_full_flush(disable: bool | None = None)</h3><p>If <code>disable</code> is <code>True</code> then automatic framebuffer flushing mentioned in <code>set_framebuffers</code> is disabled. This removes any time limit on frames in the frame buffer fifo. For example, if you set the number of frame buffers to 30 and set the frame rate to 30 you can now precisely record 1 second of video from the camera without risk of frame loss.</p><p>If this function is called with no arguments it returns if automatic flushing is disabled. By default automatic flushing on frame drop is enabled to clear out stale frames.</p><div><p>Note</p><p><code>snapshot</code> starts the frame capture process which will continue to capture frames until there is no space to hold a frame at which point the frame capture process stops. The process always stops when there is no space to hold the next frame.</p></div>
    """
    pass
def set_lens_correction(enable:bool, radi:int, coef:int) -> None:
    """
    <h3>sensor - set_lens_correction(enable: bool, radi: int, coef: int)</h3><p><code>enable</code> True to enable and False to disable (bool). <code>radi</code> integer radius of pixels to correct (int). <code>coef</code> power of correction (int).</p>
    """
    pass
def set_vsync_callback(cb) -> None:
    """
    <h3>sensor - set_vsync_callback(cb)</h3><p>Registers callback <code>cb</code> to be executed (in interrupt context) whenever the camera module generates a new frame (but, before the frame is received).</p><p><code>cb</code> takes one argument and is passed the current state of the vsync pin after changing.</p>
    """
    pass
def set_frame_callback(cb) -> None:
    """
    <h3>sensor - set_frame_callback(cb)</h3><p>Registers callback <code>cb</code> to be executed (in interrupt context) whenever the camera module generates a new frame and the frame is ready to be read via <code>sensor.snapshot()</code>.</p><p><code>cb</code> takes no arguments.</p><p>Use this to get an interrupt to schedule reading a frame later with <code>micropython.schedule()</code>.</p>
    """
    pass
def get_frame_available() -> bool:
    """
    <h3>sensor - get_frame_available()</h3><p>Returns True if a frame is available to read by calling <code>sensor.snapshot()</code>.</p>
    """
    pass
def ioctl(*args, **kwargs) -> Any:
    """
    <h3>sensor - ioctl(*args, **kwargs)</h3><p>Executes a sensor specific method:</p><ul><li><dl><dt><code>sensor.IOCTL_SET_READOUT_WINDOW</code> - Pass this enum followed by a rect tuple (x, y, w, h) or a size tuple (w, h).</dt><dd><ul><li>This IOCTL allows you to control the readout window of the camera sensor which dramatically improves the frame rate at the cost of field-of-view.</li><li>If you pass a rect tuple (x, y, w, h) the readout window will be positoned on that rect tuple. The rect tuple’s x/y position will be adjusted so the size w/h fits. Additionally, the size w/h will be adjusted to not be smaller than the <code>framesize</code>.</li><li>If you pass a size tuple (w, h) the readout window will be centered given the w/h. Additionally, the size w/h will be adjusted to not be smaller than the <code>framesize</code>.</li><li>This IOCTL is extremely helpful for increasing the frame rate on higher resolution cameras like the OV2640/OV5640.</li></ul>
    """
    pass
def set_color_palette(palette:int) -> None:
    """
    <h3>sensor - set_color_palette(palette: int)</h3><p>Sets the color palette to use for FLIR Lepton grayscale to RGB565 conversion.</p>
    """
    pass
def get_color_palette() -> int:
    """
    <h3>sensor - get_color_palette()</h3><p>Returns the current color palette setting. Defaults to <code>image.PALETTE_RAINBOW</code>.</p>
    """
    pass
def __write_reg(address:int, value:int) -> None:
    """
    <h3>sensor - __write_reg(address: int, value: int)</h3><p>Write <code>value</code> (int) to camera register at <code>address</code> (int).</p><div><p>Note</p><p>See the camera data sheet for register info.</p></div>
    """
    pass
def __read_reg(address:int) -> int:
    """
    <h3>sensor - __read_reg(address: int)</h3><p>Read camera register at <code>address</code> (int).</p><div><p>Note</p><p>See the camera data sheet for register info.</p></div>
    """
    pass
