from __future__ import annotations
from typing import List, Tuple, Union, Any, Optional
import image
"""
<h3>machine - mem8</h3><p>Read/write 8 bits of memory.</p>
"""
mem8 = None
"""
<h3>machine - mem16</h3><p>Read/write 16 bits of memory.</p>
"""
mem16 = None
"""
<h3>machine - mem32</h3><p>Read/write 32 bits of memory.</p>
"""
mem32 = None
def reset():
    """
    <h3>machine - reset()</h3><p>Resets the device in a manner similar to pushing the external RESET button.</p>
    """
    pass
def soft_reset():
    """
    <h3>machine - soft_reset()</h3><p>Performs a soft reset of the interpreter, deleting all Python objects and resetting the Python heap. It tries to retain the method by which the user is connected to the MicroPython REPL (eg serial, USB, Wifi).</p>
    """
    pass
def reset_cause():
    """
    <h3>machine - reset_cause()</h3><p>Get the reset cause. See constants for the possible return values.</p>
    """
    pass
def bootloader(value):
    """
    <h3>machine - bootloader([value])</h3><p>Reset the device and enter its bootloader. This is typically used to put the device into a state where it can be programmed with new firmware.</p><p>Some ports support passing in an optional <em>value</em> argument which can control which bootloader to enter, what to pass to it, or other things.</p>
    """
    pass
def disable_irq():
    """
    <h3>machine - disable_irq()</h3><p>Disable interrupt requests. Returns the previous IRQ state which should be considered an opaque value. This return value should be passed to the <code>enable_irq()</code> function to restore interrupts to their original state, before <code>disable_irq()</code> was called.</p>
    """
    pass
def enable_irq(state):
    """
    <h3>machine - enable_irq(state)</h3><p>Re-enable interrupt requests. The <em>state</em> parameter should be the value that was returned from the most recent call to the <code>disable_irq()</code> function.</p>
    """
    pass
def freq(hz):
    """
    <h3>machine - freq([hz])</h3><p>Returns the CPU frequency in hertz.</p><p>On some ports this can also be used to set the CPU frequency by passing in <em>hz</em>.</p>
    """
    pass
def idle():
    """
    <h3>machine - idle()</h3><p>Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered, or at most one millisecond after the CPU was paused.</p><p>It is recommended to call this function inside any tight loop that is continuously checking for an external change (i.e. polling). This will reduce power consumption without significantly impacting performance. To reduce power consumption further then see the <code>lightsleep()</code>, <code>time.sleep()</code> and <code>time.sleep_ms()</code> functions.</p>
    """
    pass
def sleep():
    """
    <h3>machine - sleep()</h3><div><p>Note</p><p>This function is deprecated, use <code>lightsleep()</code> instead with no arguments.</p></div>
    """
    pass
def deepsleep(time_ms):
    """
    <h3>machine - deepsleep([time_ms])</h3><p>Stops execution in an attempt to enter a low power state.</p><p>If <em>time_ms</em> is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.</p><p>With or without a timeout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like <code>Pin</code> change or <code>RTC</code> timeout.</p><p>The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:</p><ul><li>A lightsleep has full RAM and state retention. Upon wake execution is resumed from the point where the sleep was requested, with all subsystems operational.</li><li>A deepsleep may not retain RAM or any other state of the system (for example peripherals or network interfaces). Upon wake execution is resumed from the main script, similar to a hard or power-on reset. The <code>reset_cause()</code> function will return <code>machine.DEEPSLEEP</code> and this can be used to distinguish a deepsleep wake from other resets.</li></ul>
    """
    pass
def lightsleep(time_ms):
    """
    <h3>machine - lightsleep([time_ms])</h3><p>Stops execution in an attempt to enter a low power state.</p><p>If <em>time_ms</em> is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.</p><p>With or without a timeout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like <code>Pin</code> change or <code>RTC</code> timeout.</p><p>The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:</p><ul><li>A lightsleep has full RAM and state retention. Upon wake execution is resumed from the point where the sleep was requested, with all subsystems operational.</li><li>A deepsleep may not retain RAM or any other state of the system (for example peripherals or network interfaces). Upon wake execution is resumed from the main script, similar to a hard or power-on reset. The <code>reset_cause()</code> function will return <code>machine.DEEPSLEEP</code> and this can be used to distinguish a deepsleep wake from other resets.</li></ul>
    """
    pass
def unique_id():
    """
    <h3>machine - unique_id()</h3><p>Returns a byte string with a unique identifier of a board/SoC. It will vary from a board/SoC instance to another, if underlying hardware allows. Length varies by hardware (so use substring of a full value if you expect a short ID). In some MicroPython ports, ID corresponds to the network MAC address.</p>
    """
    pass
def time_pulse_us(pin, pulse_level, timeout_us=1000000, /):
    """
    <h3>machine - time_pulse_us(pin, pulse_level, timeout_us=1000000, /)</h3><p>Time a pulse on the given <em>pin</em>, and return the duration of the pulse in microseconds. The <em>pulse_level</em> argument should be 0 to time a low pulse or 1 to time a high pulse.</p><p>If the current input value of the pin is different to <em>pulse_level</em>, the function first (*) waits until the pin input becomes equal to <em>pulse_level</em>, then (**) times the duration that the pin is equal to <em>pulse_level</em>. If the pin is already equal to <em>pulse_level</em> then timing starts straight away.</p><p>The function will return -2 if there was timeout waiting for condition marked (*) above, and -1 if there was timeout during the main measurement, marked (**) above. The timeout is the same for both cases and given by <em>timeout_us</em> (which is in microseconds).</p>
    """
    pass
def bitstream(pin, encoding, timing, data, /):
    """
    <h3>machine - bitstream(pin, encoding, timing, data, /)</h3><p>Transmits <em>data</em> by bit-banging the specified <em>pin</em>. The <em>encoding</em> argument specifies how the bits are encoded, and <em>timing</em> is an encoding-specific timing specification.</p><p>The supported encodings are:</p><div><ul><li><code>0</code> for “high low” pulse duration modulation. This will transmit 0 and 1 bits as timed pulses, starting with the most significant bit. The <em>timing</em> must be a four-tuple of nanoseconds in the format <code>(high_time_0, low_time_0, high_time_1, low_time_1)</code>. For example, <code>(400, 850, 800, 450)</code> is the timing specification for WS2812 RGB LEDs at 800kHz.</li></ul></div><p>The accuracy of the timing varies between ports. On Cortex M0 at 48MHz, it is at best +/- 120ns, however on faster MCUs (ESP8266, ESP32, STM32, Pyboard), it will be closer to +/-30ns.</p><div><p>Note</p><p>For controlling WS2812 / NeoPixel strips, see the <code>neopixel</code> module for a higher-level API.</p></div>
    """
    pass
class ADC:
    def __init__(self, id, *, sample_ns, atten):
        """
        <h3>machine - ADC(id, *, sample_ns, atten)</h3><p>Access the ADC associated with a source identified by <em>id</em>. This <em>id</em> may be an integer (usually specifying a channel number), a Pin object, or other value supported by the underlying machine.</p><p>If additional keyword-arguments are given then they will configure various aspects of the ADC. If not given, these settings will take previous or default values. The settings are:</p><div><ul><li><em>sample_ns</em> is the sampling time in nanoseconds.</li><li><em>atten</em> specifies the input attenuation.</li></ul></div>
        """
        pass
    def init(self, *, sample_ns, atten):
        """
        <h3>machine - ADC.init(*, sample_ns, atten)</h3><p>Apply the given settings to the ADC. Only those arguments that are specified will be changed. See the ADC constructor above for what the arguments are.</p>
        """
        pass
    def block(self):
        """
        <h3>machine - ADC.block()</h3><p>Return the ADCBlock instance associated with this ADC object.</p><p>This method only exists if the port supports the ADCBlock class.</p>
        """
        pass
    def read_u16(self):
        """
        <h3>machine - ADC.read_u16()</h3><p>Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.</p>
        """
        pass
    def read_uv(self):
        """
        <h3>machine - ADC.read_uv()</h3><p>Take an analog reading and return an integer value with units of microvolts. It is up to the particular port whether or not this value is calibrated, and how calibration is done.</p>
        """
        pass
class ADCBlock:
    def __init__(self, id, *, bits):
        """
        <h3>machine - ADCBlock(id, *, bits)</h3><p>Access the ADC peripheral identified by <em>id</em>, which may be an integer or string.</p><p>The <em>bits</em> argument, if given, sets the resolution in bits of the conversion process. If not specified then the previous or default resolution is used.</p>
        """
        pass
    def init(self, *, bits):
        """
        <h3>machine - ADCBlock.init(*, bits)</h3><p>Configure the ADC peripheral. <em>bits</em> will set the resolution of the conversion process.</p>
        """
        pass
    def connect(self, channel, *):
        """
        <h3>machine - ADCBlock.connect(channel, *, ...)</h3><p>Connect up a channel on the ADC peripheral so it is ready for sampling, and return an ADC object that represents that connection.</p><p>The <em>channel</em> argument must be an integer, and <em>source</em> must be an object (for example a Pin) which can be connected up for sampling.</p><p>If only <em>channel</em> is given then it is configured for sampling.</p><p>If only <em>source</em> is given then that object is connected to a default channel ready for sampling.</p><p>If both <em>channel</em> and <em>source</em> are given then they are connected together and made ready for sampling.</p><p>Any additional keyword arguments are used to configure the returned ADC object, via its <code>init</code> method.</p>
        """
        pass
class CAN:
    def __init__(self, bus):
        """
        <h3>machine - CAN(bus, ...)</h3><p>Construct a CAN object on the given bus. <em>bus</em> can be 0. With no additional parameters, the CAN object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See <code>CAN.init()</code> for parameters of initialisation.</p><p>The physical pins of the CAN buses are:</p><div><ul><li><code>CAN(0)</code>: <code>(RX, TX) = (P3, P1)</code></li></ul></div>
        """
        pass
    def init(self, mode, *, auto_restart=False, baudrate=0):
        """
        <h3>machine - CAN.init(mode, *, auto_restart=False, baudrate=0)</h3><p>Initialise the CAN bus with the given parameters:</p><div><ul><li><em>mode</em> is one of: NORMAL, LOOPBACK, SILENT, SILENT_LOOPBACK</li><li><em>auto_restart</em> sets whether the controller will automatically try and restart communications after entering the bus-off state; if this is disabled then <code>restart()</code> can be used to leave the bus-off state</li><li><em>baudrate</em> sets the baudrate used to connect to the CAN bus</li></ul></div>
        """
        pass
    def deinit(self):
        """
        <h3>machine - CAN.deinit()</h3><p>Turn off the CAN bus.</p>
        """
        pass
    def restart(self):
        """
        <h3>machine - CAN.restart()</h3><p>Force a software restart of the CAN controller without resetting its configuration.</p><p>If the controller enters the bus-off state then it will no longer participate in bus activity. If the controller is not configured to automatically restart (see <code>init()</code>) then this method can be used to trigger a restart, and the controller will follow the CAN protocol to leave the bus-off state and go into the error active state.</p>
        """
        pass
    def state(self):
        """
        <h3>machine - CAN.state()</h3><p>Return the state of the controller. The return value can be one of:</p><ul><li><code>CAN.STOPPED</code> – the controller is completely off and reset;</li><li><code>CAN.ERROR_ACTIVE</code> – the controller is on and in the Error Active state (both TEC and REC are less than 96);</li><li><code>CAN.ERROR_WARNING</code> – the controller is on and in the Error Warning state (at least one of TEC or REC is 96 or greater);</li><li><code>CAN.ERROR_PASSIVE</code> – the controller is on and in the Error Passive state (at least one of TEC or REC is 128 or greater);</li><li><code>CAN.BUS_OFF</code> – the controller is on but not participating in bus activity (TEC overflowed beyond 255).</li></ul>
        """
        pass
    def info(self, list):
        """
        <h3>machine - CAN.info([list])</h3><p>Get information about the controller’s error states and TX and RX buffers. If <em>list</em> is provided then it should be a list object with at least 8 entries, which will be filled in with the information. Otherwise a new list will be created and filled in. In both cases the return value of the method is the populated list.</p><p>The values in the list are:</p><ul><li>TEC value</li><li>REC value</li><li>number of times the controller enterted the Error Warning state (wrapped around to 0 after 65535)</li><li>number of times the controller enterted the Error Passive state (wrapped around to 0 after 65535)</li><li>number of times the controller enterted the Bus Off state (wrapped around to 0 after 65535)</li><li>number of pending TX messages</li><li>number of pending RX messages on fifo 0</li><li>always 0</li></ul>
        """
        pass
    def setfilter(self, bank, mode, fifo, params, *, rtr, extframe=False):
        """
        <h3>machine - CAN.setfilter(bank, mode, fifo, params, *, rtr, extframe=False)</h3><p>Configure a filter bank:</p><ul><li><em>bank</em> is the classic CAN controller filter bank to configure.</li><li><em>mode</em> is the mode the filter should operate in, see the tables below.</li><li><em>fifo</em> is which fifo (0) a message should be stored in, if it is accepted by this filter.</li><li><em>params</em> is an array of values the defines the filter. The contents of the array depends on the <em>mode</em> argument.</li></ul><table><thead><tr><th><p><em>mode</em></p></th><th><p>Contents of <em>params</em> array for classic CAN controller</p></th></tr></thead><tbody><tr><td><p>CAN.LIST32</p></td><td><p>Two 32 bit ids that will be accepted</p></td></tr><tr><td><p>CAN.DUAL</p></td><td><p>Two ids that will be accepted. For example (1, 2)</p></td></tr></tbody></table><ul><li><em>rtr</em> For classic CAN controllers, this is an array of booleans that states if a filter should accept a remote transmission request message. If this argument is not given then it defaults to <code>False</code> for all entries. The length of the array depends on the <em>mode</em> argument.</li></ul><table><thead><tr><th><p><em>mode</em></p></th><th><p>length of <em>rtr</em> array</p></th></tr></thead><tbody><tr><td><p>CAN.LIST32</p></td><td><p>2</p></td></tr><tr><td><p>CAN.DUAL</p></td><td><p>2</p></td></tr></tbody></table><ul><li><em>extframe</em> If True the frame will have an extended identifier (29 bits), otherwise a standard identifier (11 bits) is used.</li></ul>
        """
        pass
    def clearfilter(self, bank, extframe=False):
        """
        <h3>machine - CAN.clearfilter(bank, extframe=False)</h3><p>Clear and disables a filter bank:</p><ul><li><em>bank</em> is the classic CAN controller filter bank to clear.</li><li><em>extframe</em> ignored</li></ul>
        """
        pass
    def any(self, fifo):
        """
        <h3>machine - CAN.any(fifo)</h3><p>Return <code>True</code> if any message waiting on the FIFO, else <code>False</code>.</p>
        """
        pass
    def recv(self, fifo, list=None, *, timeout=5000):
        """
        <h3>machine - CAN.recv(fifo, list=None, *, timeout=5000)</h3><p>Receive data on the bus:</p><div><ul><li><em>fifo</em> is an integer, which is the FIFO to receive on - always 0</li><li><em>list</em> is an optional list object to be used as the return value</li><li><em>timeout</em> is the timeout in milliseconds to wait for the receive.</li></ul></div><p>Return value: A tuple containing five values.</p><div><ul><li>The id of the message.</li><li>A boolean that indicates if the message ID is standard or extended.</li><li>A boolean that indicates if the message is an RTR message.</li><li>The FMI (Filter Match Index) value.</li><li>An array containing the data.</li></ul></div><p>If <em>list</em> is <code>None</code> then a new tuple will be allocated, as well as a new bytes object to contain the data (as the fifth element in the tuple).</p><p>If <em>list</em> is not <code>None</code> then it should be a list object with a least five elements. The fifth element should be a memoryview object which is created from either a bytearray or an array of type ‘B’ or ‘b’, and this array must have enough room for at least 8 bytes. The list object will then be populated with the first four return values above, and the memoryview object will be resized inplace to the size of the data and filled in with that data. The same list and memoryview objects can be reused in subsequent calls to this method, providing a way of receiving data without using the heap. For example:</p><div><div><pre>buf = bytearray(8) lst = [0, 0, 0, 0, memoryview(buf)] # No heap memory is allocated in the following call can.recv(0, lst) </pre></div></div>
        """
        pass
    def send(self, data, id, *, timeout=0, rtr=False, extframe=False):
        """
        <h3>machine - CAN.send(data, id, *, timeout=0, rtr=False, extframe=False)</h3><p>Send a message on the bus:</p><div><ul><li><em>data</em> is the data to send (an integer to send, or a buffer object).</li><li><em>id</em> is the id of the message to be sent.</li><li><em>timeout</em> is the timeout in milliseconds to wait for the send.</li><li><em>rtr</em> is a boolean that specifies if the message shall be sent as a remote transmission request. If <em>rtr</em> is True then only the length of <em>data</em> is used to fill in the DLC slot of the frame; the actual bytes in <em>data</em> are unused.</li><li><em>extframe</em> if True the frame will have an extended identifier (29 bits), otherwise a standard identifier (11 bits) is used.</li></ul><dl><dt>If timeout is 0 the message is placed in a buffer and the method returns immediately.</dt><dd><p>If all three buffers are in use an exception is thrown. If timeout is not 0, the method waits until the message is transmitted. If the message can’t be transmitted within the specified time an exception is thrown.</p>
        """
        pass
    def rxcallback(self, fifo, fun):
        """
        <h3>machine - CAN.rxcallback(fifo, fun)</h3><p>Register a function to be called when a message is accepted into a empty fifo:</p><ul><li><em>fifo</em> is the receiving fifo - always 0.</li><li><em>fun</em> is the function to be called when the fifo becomes non empty.</li></ul><p>The callback function takes two arguments the first is the can object it self the second is a integer that indicates the reason for the callback.</p><table><thead><tr><th><p>Reason</p></th><th></th></tr></thead><tbody><tr><td><p>0</p></td><td><p>A message has been accepted into a empty FIFO.</p></td></tr><tr><td><p>1</p></td><td><p>The FIFO is full</p></td></tr><tr><td><p>2</p></td><td><p>A message has been lost due to a full FIFO</p></td></tr></tbody></table><p>Example use of rxcallback:</p><div><div><pre>def cb0(bus, reason): print(&#39;cb0&#39;) if reason == 0: print(&#39;pending&#39;) if reason == 1: print(&#39;full&#39;) if reason == 2: print(&#39;overflow&#39;) can = CAN(0, CAN.LOOPBACK) can.rxcallback(0, cb0) </pre></div></div>
        """
        pass
class I2C:
    def __init__(self, id, *, scl, sda, freq=400000, timeout=50000):
        """
        <h3>machine - I2C(id, *, scl, sda, freq=400000, timeout=50000)</h3><p>Construct and return a new I2C object using the following parameters:</p><div><ul><li><em>id</em> identifies a particular I2C peripheral. Allowed values for depend on the particular port/board</li><li><em>scl</em> should be a pin object specifying the pin to use for SCL.</li><li><em>sda</em> should be a pin object specifying the pin to use for SDA.</li><li><em>freq</em> should be an integer which sets the maximum frequency for SCL.</li><li><em>timeout</em> is the maximum time in microseconds to allow for I2C transactions. This parameter is not allowed on some ports.</li></ul></div><p>Note that some ports/boards will have default values of <em>scl</em> and <em>sda</em> that can be changed in this constructor. Others will have fixed values of <em>scl</em> and <em>sda</em> that cannot be changed.</p>
        """
        pass
    def init(self, scl, sda, *, freq=400000):
        """
        <h3>machine - I2C.init(scl, sda, *, freq=400000)</h3><p>Initialise the I2C bus with the given arguments:</p><div><div><ul><li><em>scl</em> is a pin object for the SCL line</li><li><em>sda</em> is a pin object for the SDA line</li><li><em>freq</em> is the SCL clock rate</li></ul></div><p>In the case of hardware I2C the actual clock frequency may be lower than the requested frequency. This is dependent on the platform hardware. The actual rate may be determined by printing the I2C object.</p></div>
        """
        pass
    def scan(self):
        """
        <h3>machine - I2C.scan()</h3><p>Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of those that respond. A device responds if it pulls the SDA line low after its address (including a write bit) is sent on the bus.</p>
        """
        pass
    def start(self):
        """
        <h3>machine - I2C.start()</h3><p>Generate a START condition on the bus (SDA transitions to low while SCL is high).</p>
        """
        pass
    def stop(self):
        """
        <h3>machine - I2C.stop()</h3><p>Generate a STOP condition on the bus (SDA transitions to high while SCL is high).</p>
        """
        pass
    def readinto(self, buf, nack=True, /):
        """
        <h3>machine - I2C.readinto(buf, nack=True, /)</h3><p>Reads bytes from the bus and stores them into <em>buf</em>. The number of bytes read is the length of <em>buf</em>. An ACK will be sent on the bus after receiving all but the last byte. After the last byte is received, if <em>nack</em> is true then a NACK will be sent, otherwise an ACK will be sent (and in this case the peripheral assumes more bytes are going to be read in a later call).</p>
        """
        pass
    def write(self, buf):
        """
        <h3>machine - I2C.write(buf)</h3><p>Write the bytes from <em>buf</em> to the bus. Checks that an ACK is received after each byte and stops transmitting the remaining bytes if a NACK is received. The function returns the number of ACKs that were received.</p>
        """
        pass
    def readfrom(self, addr, nbytes, stop=True, /):
        """
        <h3>machine - I2C.readfrom(addr, nbytes, stop=True, /)</h3><p>Read <em>nbytes</em> from the peripheral specified by <em>addr</em>. If <em>stop</em> is true then a STOP condition is generated at the end of the transfer. Returns a <code>bytes</code> object with the data read.</p>
        """
        pass
    def readfrom_into(self, addr, buf, stop=True, /):
        """
        <h3>machine - I2C.readfrom_into(addr, buf, stop=True, /)</h3><p>Read into <em>buf</em> from the peripheral specified by <em>addr</em>. The number of bytes read will be the length of <em>buf</em>. If <em>stop</em> is true then a STOP condition is generated at the end of the transfer.</p><p>The method returns <code>None</code>.</p>
        """
        pass
    def writeto(self, addr, buf, stop=True, /):
        """
        <h3>machine - I2C.writeto(addr, buf, stop=True, /)</h3><p>Write the bytes from <em>buf</em> to the peripheral specified by <em>addr</em>. If a NACK is received following the write of a byte from <em>buf</em> then the remaining bytes are not sent. If <em>stop</em> is true then a STOP condition is generated at the end of the transfer, even if a NACK is received. The function returns the number of ACKs that were received.</p>
        """
        pass
    def writevto(self, addr, vector, stop=True, /):
        """
        <h3>machine - I2C.writevto(addr, vector, stop=True, /)</h3><p>Write the bytes contained in <em>vector</em> to the peripheral specified by <em>addr</em>. <em>vector</em> should be a tuple or list of objects with the buffer protocol. The <em>addr</em> is sent once and then the bytes from each object in <em>vector</em> are written out sequentially. The objects in <em>vector</em> may be zero bytes in length in which case they don’t contribute to the output.</p><p>If a NACK is received following the write of a byte from one of the objects in <em>vector</em> then the remaining bytes, and any remaining objects, are not sent. If <em>stop</em> is true then a STOP condition is generated at the end of the transfer, even if a NACK is received. The function returns the number of ACKs that were received.</p>
        """
        pass
    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
        """
        <h3>machine - I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)</h3><p>Read <em>nbytes</em> from the peripheral specified by <em>addr</em> starting from the memory address specified by <em>memaddr</em>. The argument <em>addrsize</em> specifies the address size in bits. Returns a <code>bytes</code> object with the data read.</p>
        """
        pass
    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8):
        """
        <h3>machine - I2C.readfrom_mem_into(addr, memaddr, buf, *, addrsize=8)</h3><p>Read into <em>buf</em> from the peripheral specified by <em>addr</em> starting from the memory address specified by <em>memaddr</em>. The number of bytes read is the length of <em>buf</em>. The argument <em>addrsize</em> specifies the address size in bits.</p><p>The method returns <code>None</code>.</p>
        """
        pass
    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8):
        """
        <h3>machine - I2C.writeto_mem(addr, memaddr, buf, *, addrsize=8)</h3><p>Write <em>buf</em> to the peripheral specified by <em>addr</em> starting from the memory address specified by <em>memaddr</em>. The argument <em>addrsize</em> specifies the address size in bits.</p><p>The method returns <code>None</code>.</p>
        """
        pass
class SoftI2C:
    def __init__(self, scl, sda, *, freq=400000, timeout=50000):
        """
        <h3>machine - SoftI2C(scl, sda, *, freq=400000, timeout=50000)</h3><p>Construct a new software I2C object. The parameters are:</p><div><ul><li><em>scl</em> should be a pin object specifying the pin to use for SCL.</li><li><em>sda</em> should be a pin object specifying the pin to use for SDA.</li><li><em>freq</em> should be an integer which sets the maximum frequency for SCL.</li><li><em>timeout</em> is the maximum time in microseconds to wait for clock stretching (SCL held low by another device on the bus), after which an <code>OSError(ETIMEDOUT)</code> exception is raised.</li></ul></div>
        """
        pass
class I2S:
    def __init__(self, id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf):
        """
        <h3>machine - I2S(id, *, sck, ws, sd, mck=None, mode, bits, format, rate, ibuf)</h3><p>Construct an I2S object of the given id:</p><ul><li><code>id</code> identifies a particular I2S bus; it is board and port specific</li></ul><p>Keyword-only parameters that are supported on all ports:</p><div><ul><li><code>sck</code> is a pin object for the serial clock line</li><li><code>ws</code> is a pin object for the word select line</li><li><code>sd</code> is a pin object for the serial data line</li><li><code>mck</code> is a pin object for the master clock line; master clock frequency is sampling rate * 256</li><li><code>mode</code> specifies receive or transmit</li><li><code>bits</code> specifies sample size (bits), 16 or 32</li><li><code>format</code> specifies channel format, STEREO or MONO</li><li><code>rate</code> specifies audio sampling rate (Hz); this is the frequency of the <code>ws</code> signal</li><li><code>ibuf</code> specifies internal buffer length (bytes)</li></ul></div><p>For all ports, DMA runs continuously in the background and allows user applications to perform other operations while sample data is transferred between the internal buffer and the I2S peripheral unit. Increasing the size of the internal buffer has the potential to increase the time that user applications can perform non-I2S operations before underflow (e.g. <code>write</code> method) or overflow (e.g. <code>readinto</code> method).</p>
        """
        pass
    def init(self, sck):
        """
        <h3>machine - I2S.init(sck, ...)</h3><p>see Constructor for argument descriptions</p>
        """
        pass
    def deinit(self):
        """
        <h3>machine - I2S.deinit()</h3><p>Deinitialize the I2S bus</p>
        """
        pass
    def readinto(self, buf):
        """
        <h3>machine - I2S.readinto(buf)</h3><p>Read audio samples into the buffer specified by <code>buf</code>. <code>buf</code> must support the buffer protocol, such as bytearray or array. “buf” byte ordering is little-endian. For Stereo format, left channel sample precedes right channel sample. For Mono format, the left channel sample data is used. Returns number of bytes read</p>
        """
        pass
    def write(self, buf):
        """
        <h3>machine - I2S.write(buf)</h3><p>Write audio samples contained in <code>buf</code>. <code>buf</code> must support the buffer protocol, such as bytearray or array. “buf” byte ordering is little-endian. For Stereo format, left channel sample precedes right channel sample. For Mono format, the sample data is written to both the right and left channels. Returns number of bytes written</p>
        """
        pass
    def irq(self, handler):
        """
        <h3>machine - I2S.irq(handler)</h3><p>Set a callback. <code>handler</code> is called when <code>buf</code> is emptied (<code>write</code> method) or becomes full (<code>readinto</code> method). Setting a callback changes the <code>write</code> and <code>readinto</code> methods to non-blocking operation. <code>handler</code> is called in the context of the MicroPython scheduler.</p>
        """
        pass
    def shift(self, *, buf, bits, shift):
        """
        <h3>machine - I2S.shift(*, buf, bits, shift)</h3><p>bitwise shift of all samples contained in <code>buf</code>. <code>bits</code> specifies sample size in bits. <code>shift</code> specifies the number of bits to shift each sample. Positive for left shift, negative for right shift. Typically used for volume control. Each bit shift changes sample volume by 6dB.</p>
        """
        pass
class LED:
    def __init__(self, pin_name) -> LED:
        """
        <h3>machine - LED(pin_name)</h3><p>Access the LED associated with a source identified by <em>pin_name</em>. This <code>pin_name</code> may be a string (usually specifying a color), a Pin object, or other value supported by the underlying machine.</p>
        """
        pass
    def boardname(self) -> str:
        """
        <h3>machine - LED.boardname()</h3><p>Returns the name of the board.</p>
        """
        pass
    def on(self) -> None:
        """
        <h3>machine - LED.on()</h3><p>Turns the LED on.</p>
        """
        pass
    def toggle(self) -> None:
        """
        <h3>machine - LED.toggle()</h3><p>Toggles the LED state.</p>
        """
        pass
    def value(self, v=None) -> int:
        """
        <h3>machine - LED.value(v=None)</h3><p>If <code>v</code> is given, sets the LED to the given value. If <code>v</code> is not given, returns the current LED value.</p>
        """
        pass
class Pin:
    def __init__(self, id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1):
        """
        <h3>machine - Pin(id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1)</h3><p>Access the pin peripheral (GPIO pin) associated with the given <code>id</code>. If additional arguments are given in the constructor then they are used to initialise the pin. Any settings that are not specified will remain in their previous state.</p><p>The arguments are:</p><div><ul><li><code>id</code> is mandatory and can be an arbitrary object. Among possible value types are: int (an internal Pin identifier), str (a Pin name), and tuple (pair of [port, pin]).</li><li><code>mode</code> specifies the pin mode, which can be one of:</p><ul><li><code>Pin.IN</code> - Pin is configured for input. If viewed as an output the pin is in high-impedance state.</li><li><code>Pin.OUT</code> - Pin is configured for (normal) output.</li><li><code>Pin.OPEN_DRAIN</code> - Pin is configured for open-drain output. Open-drain output works in the following way: if the output value is set to 0 the pin is active at a low level; if the output value is 1 the pin is in a high-impedance state. Not all ports implement this mode, or some might only on certain pins.</li><li><code>Pin.ALT</code> - Pin is configured to perform an alternative function, which is port specific. For a pin configured in such a way any other Pin methods (except <code>Pin.init()</code>) are not applicable (calling them will lead to undefined, or a hardware-specific, result). Not all ports implement this mode.</li><li><code>Pin.ALT_OPEN_DRAIN</code> - The Same as <code>Pin.ALT</code>, but the pin is configured as open-drain. Not all ports implement this mode.</li><li><code>Pin.ANALOG</code> - Pin is configured for analog input, see the <code>ADC</code> class.</li></ul></li><li><code>pull</code> specifies if the pin has a (weak) pull resistor attached, and can be one of:</p><ul><li><code>None</code> - No pull up or down resistor.</li><li><code>Pin.PULL_UP</code> - Pull up resistor enabled.</li><li><code>Pin.PULL_DOWN</code> - Pull down resistor enabled.</li></ul></li><li><code>value</code> is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial output pin value if given, otherwise the state of the pin peripheral remains unchanged.</li><li><code>drive</code> specifies the output power of the pin and can be one of: <code>Pin.DRIVE_0</code>, <code>Pin.DRIVE_1</code>, etc., increasing in drive strength. The actual current driving capabilities are port dependent. Not all ports implement this argument.</li><li><code>alt</code> specifies an alternate function for the pin and the values it can take are port dependent. This argument is valid only for <code>Pin.ALT</code> and <code>Pin.ALT_OPEN_DRAIN</code> modes. It may be used when a pin supports more than one alternate function. If only one pin alternate function is supported the this argument is not required. Not all ports implement this argument.</li></ul></div><p>As specified above, the Pin class allows to set an alternate function for a particular pin, but it does not specify any further operations on such a pin. Pins configured in alternate-function mode are usually not used as GPIO but are instead driven by other hardware peripherals. The only operation supported on such a pin is re-initialising, by calling the constructor or <code>Pin.init()</code> method. If a pin that is configured in alternate-function mode is re-initialised with <code>Pin.IN</code>, <code>Pin.OUT</code>, or <code>Pin.OPEN_DRAIN</code>, the alternate function will be removed from the pin.</p>
        """
        pass
    def init(self, mode=-1, pull=-1, *, value=None, drive=0, alt=-1):
        """
        <h3>machine - Pin.init(mode=-1, pull=-1, *, value=None, drive=0, alt=-1)</h3><p>Re-initialise the pin using the given parameters. Only those arguments that are specified will be set. The rest of the pin peripheral state will remain unchanged. See the constructor documentation for details of the arguments.</p><p>Returns <code>None</code>.</p>
        """
        pass
    def value(self, x):
        """
        <h3>machine - Pin.value([x])</h3><p>This method allows to set and get the value of the pin, depending on whether the argument <code>x</code> is supplied or not.</p><p>If the argument is omitted then this method gets the digital logic level of the pin, returning 0 or 1 corresponding to low and high voltage signals respectively. The behaviour of this method depends on the mode of the pin:</p><div><ul><li><code>Pin.IN</code> - The method returns the actual input value currently present on the pin.</li><li><code>Pin.OUT</code> - The behaviour and return value of the method is undefined.</li><li><code>Pin.OPEN_DRAIN</code> - If the pin is in state ‘0’ then the behaviour and return value of the method is undefined. Otherwise, if the pin is in state ‘1’, the method returns the actual input value currently present on the pin.</li></ul></div><p>If the argument is supplied then this method sets the digital logic level of the pin. The argument <code>x</code> can be anything that converts to a boolean. If it converts to <code>True</code>, the pin is set to state ‘1’, otherwise it is set to state ‘0’. The behaviour of this method depends on the mode of the pin:</p><div><ul><li><code>Pin.IN</code> - The value is stored in the output buffer for the pin. The pin state does not change, it remains in the high-impedance state. The stored value will become active on the pin as soon as it is changed to <code>Pin.OUT</code> or <code>Pin.OPEN_DRAIN</code> mode.</li><li><code>Pin.OUT</code> - The output buffer is set to the given value immediately.</li><li><code>Pin.OPEN_DRAIN</code> - If the value is ‘0’ the pin is set to a low voltage state. Otherwise the pin is set to high-impedance state.</li></ul></div><p>When setting the value this method returns <code>None</code>.</p>
        """
        pass
    def __call__(self, x):
        """
        <h3>machine - Pin.__call__([x])</h3><p>Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin. It is equivalent to Pin.value([x]). See <code>Pin.value()</code> for more details.</p>
        """
        pass
    def on(self):
        """
        <h3>machine - Pin.on()</h3><p>Set pin to “1” output level.</p>
        """
        pass
    def off(self):
        """
        <h3>machine - Pin.off()</h3><p>Set pin to “0” output level.</p>
        """
        pass
    def irq(self, handler=None, trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING, *, priority=1, wake=None, hard=False):
        """
        <h3>machine - Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)</h3><p>Configure an interrupt handler to be called when the trigger source of the pin is active. If the pin mode is <code>Pin.IN</code> then the trigger source is the external value on the pin. If the pin mode is <code>Pin.OUT</code> then the trigger source is the output buffer of the pin. Otherwise, if the pin mode is <code>Pin.OPEN_DRAIN</code> then the trigger source is the output buffer for state ‘0’ and the external pin value for state ‘1’.</p><p>The arguments are:</p><div><ul><li><code>handler</code> is an optional function to be called when the interrupt triggers. The handler must take exactly one argument which is the <code>Pin</code> instance.</li><li><code>trigger</code> configures the event which can generate an interrupt. Possible values are:</p><ul><li><code>Pin.IRQ_FALLING</code> interrupt on falling edge.</li><li><code>Pin.IRQ_RISING</code> interrupt on rising edge.</li><li><code>Pin.IRQ_LOW_LEVEL</code> interrupt on low level.</li><li><code>Pin.IRQ_HIGH_LEVEL</code> interrupt on high level.</li></ul><p>These values can be OR’ed together to trigger on multiple events.</p></li><li><code>priority</code> sets the priority level of the interrupt. The values it can take are port-specific, but higher values always represent higher priorities.</li><li><code>wake</code> selects the power mode in which this interrupt can wake up the system. It can be <code>machine.IDLE</code>, <code>machine.SLEEP</code> or <code>machine.DEEPSLEEP</code>. These values can also be OR’ed together to make a pin generate interrupts in more than one power mode.</li><li><code>hard</code> if true a hardware interrupt is used. This reduces the delay between the pin change and the handler being called. Hard interrupt handlers may not allocate memory; see Writing interrupt handlers. Not all ports support this argument.</li></ul></div><p>This method returns a callback object.</p>
        """
        pass
    def low(self):
        """
        <h3>machine - Pin.low()</h3><p>Set pin to “0” output level.</p><p>Availability: nrf, rp2, stm32 ports.</p>
        """
        pass
    def high(self):
        """
        <h3>machine - Pin.high()</h3><p>Set pin to “1” output level.</p><p>Availability: nrf, rp2, stm32 ports.</p>
        """
        pass
    def mode(self, mode):
        """
        <h3>machine - Pin.mode([mode])</h3><p>Get or set the pin mode. See the constructor documentation for details of the <code>mode</code> argument.</p><p>Availability: cc3200, stm32 ports.</p>
        """
        pass
    def pull(self, pull):
        """
        <h3>machine - Pin.pull([pull])</h3><p>Get or set the pin pull state. See the constructor documentation for details of the <code>pull</code> argument.</p><p>Availability: cc3200, stm32 ports.</p>
        """
        pass
    def drive(self, drive):
        """
        <h3>machine - Pin.drive([drive])</h3><p>Get or set the pin drive strength. See the constructor documentation for details of the <code>drive</code> argument.</p><p>Availability: cc3200 port.</p>
        """
        pass
    def toggle(self):
        """
        <h3>machine - Pin.toggle()</h3><p>Toggle output pin from “0” to “1” or vice-versa.</p><p>Availability: mimxrt, samd, rp2 ports.</p>
        """
        pass
class PWM:
    def __init__(self, dest, *, freq, duty_u16, duty_ns, invert):
        """
        <h3>machine - PWM(dest, *, freq, duty_u16, duty_ns, invert)</h3><p>Construct and return a new PWM object using the following parameters:</p><div><ul><li><em>dest</em> is the entity on which the PWM is output, which is usually a machine.Pin object, but a port may allow other values, like integers.</li><li><em>freq</em> should be an integer which sets the frequency in Hz for the PWM cycle.</li><li><em>duty_u16</em> sets the duty cycle as a ratio <code>duty_u16 / 65535</code>.</li><li><em>duty_ns</em> sets the pulse width in nanoseconds.</li><li><em>invert</em> inverts the respective output if the value is True</li></ul></div><p>Setting <em>freq</em> may affect other PWM objects if the objects share the same underlying PWM generator (this is hardware specific). Only one of <em>duty_u16</em> and <em>duty_ns</em> should be specified at a time. <em>invert</em> is not available at all ports.</p>
        """
        pass
    def init(self, *, freq, duty_u16, duty_ns):
        """
        <h3>machine - PWM.init(*, freq, duty_u16, duty_ns)</h3><p>Modify settings for the PWM object. See the above constructor for details about the parameters.</p>
        """
        pass
    def deinit(self):
        """
        <h3>machine - PWM.deinit()</h3><p>Disable the PWM output.</p>
        """
        pass
    def freq(self, value):
        """
        <h3>machine - PWM.freq([value])</h3><p>Get or set the current frequency of the PWM output.</p><p>With no arguments the frequency in Hz is returned.</p><p>With a single <em>value</em> argument the frequency is set to that value in Hz. The method may raise a <code>ValueError</code> if the frequency is outside the valid range.</p>
        """
        pass
    def duty_u16(self, value):
        """
        <h3>machine - PWM.duty_u16([value])</h3><p>Get or set the current duty cycle of the PWM output, as an unsigned 16-bit value in the range 0 to 65535 inclusive.</p><p>With no arguments the duty cycle is returned.</p><p>With a single <em>value</em> argument the duty cycle is set to that value, measured as the ratio <code>value / 65535</code>.</p>
        """
        pass
    def duty_ns(self, value):
        """
        <h3>machine - PWM.duty_ns([value])</h3><p>Get or set the current pulse width of the PWM output, as a value in nanoseconds.</p><p>With no arguments the pulse width in nanoseconds is returned.</p><p>With a single <em>value</em> argument the pulse width is set to that value.</p>
        """
        pass
class RTC:
    def __init__(self, id=0):
        """
        <h3>machine - RTC(id=0, ...)</h3><p>Create an RTC object. See init for parameters of initialization.</p>
        """
        pass
    def datetime(self, datetimetuple):
        """
        <h3>machine - RTC.datetime([datetimetuple])</h3><p>Get or set the date and time of the RTC.</p><p>With no arguments, this method returns an 8-tuple with the current date and time. With 1 argument (being an 8-tuple) it sets the date and time.</p><p>The 8-tuple has the following format:</p><div><p>(year, month, day, weekday, hours, minutes, seconds, subseconds)</p></div><p>The meaning of the <code>subseconds</code> field is hardware dependent.</p>
        """
        pass
    def init(self, datetime):
        """
        <h3>machine - RTC.init(datetime)</h3><p>Initialise the RTC. Datetime is a tuple of the form:</p><div><p><code>(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])</code></p></div>
        """
        pass
    def now(self):
        """
        <h3>machine - RTC.now()</h3><p>Get get the current datetime tuple.</p>
        """
        pass
    def deinit(self):
        """
        <h3>machine - RTC.deinit()</h3><p>Resets the RTC to the time of January 1, 2015 and starts running it again.</p>
        """
        pass
    def alarm(self, id, time, *, repeat=False):
        """
        <h3>machine - RTC.alarm(id, time, *, repeat=False)</h3><p>Set the RTC alarm. Time might be either a millisecond value to program the alarm to current time + time_in_ms in the future, or a datetimetuple. If the time passed is in milliseconds, repeat can be set to <code>True</code> to make the alarm periodic.</p>
        """
        pass
    def alarm_left(self, alarm_id=0):
        """
        <h3>machine - RTC.alarm_left(alarm_id=0)</h3><p>Get the number of milliseconds left before the alarm expires.</p>
        """
        pass
    def cancel(self, alarm_id=0):
        """
        <h3>machine - RTC.cancel(alarm_id=0)</h3><p>Cancel a running alarm.</p>
        """
        pass
    def irq(self, *, trigger, handler=None, wake=machine.IDLE):
        """
        <h3>machine - RTC.irq(*, trigger, handler=None, wake=machine.IDLE)</h3><p>Create an irq object triggered by a real time clock alarm.</p><div><ul><li><code>trigger</code> must be <code>RTC.ALARM0</code></li><li><code>handler</code> is the function to be called when the callback is triggered.</li><li><code>wake</code> specifies the sleep mode from where this interrupt can wake up the system.</li></ul></div>
        """
        pass
    def memory(self, data):
        """
        <h3>machine - RTC.memory([data])</h3><p><code>RTC.memory(data)</code> will write <em>data</em> to the RTC memory, where <em>data</em> is any object which supports the buffer protocol (including <code>bytes</code>, <code>bytearray</code>, <code>memoryview</code> and <code>array.array</code>). <code>RTC.memory()</code> reads RTC memory and returns a <code>bytes</code> object.</p><p>Data written to RTC user memory is persistent across restarts, including <code>machine.soft_reset()</code> and <code>machine.deepsleep()</code>.</p><p>The maximum length of RTC user memory is 2048 bytes by default on esp32, and 492 bytes on esp8266.</p><p>Availability: esp32, esp8266 ports.</p>
        """
        pass
class Signal:
    def __init__(self, pin_obj, invert=False):
        """
        <h3>machine - Signal(pin_obj, invert=False)</h3><p>Create a Signal object. There’re two ways to create it:</p><ul><li>By wrapping existing Pin object - universal method which works for any board.</li><li>By passing required Pin parameters directly to Signal constructor, skipping the need to create intermediate Pin object. Available on many, but not all boards.</li></ul><p>The arguments are:</p><div><ul><li><code>pin_obj</code> is existing Pin object.</li><li><code>pin_arguments</code> are the same arguments as can be passed to Pin constructor.</li><li><code>invert</code> - if True, the signal will be inverted (active low).</li></ul></div>
        """
        pass
    def value(self, x):
        """
        <h3>machine - Signal.value([x])</h3><p>This method allows to set and get the value of the signal, depending on whether the argument <code>x</code> is supplied or not.</p><p>If the argument is omitted then this method gets the signal level, 1 meaning signal is asserted (active) and 0 - signal inactive.</p><p>If the argument is supplied then this method sets the signal level. The argument <code>x</code> can be anything that converts to a boolean. If it converts to <code>True</code>, the signal is active, otherwise it is inactive.</p><p>Correspondence between signal being active and actual logic level on the underlying pin depends on whether signal is inverted (active-low) or not. For non-inverted signal, active status corresponds to logical 1, inactive - to logical 0. For inverted/active-low signal, active status corresponds to logical 0, while inactive - to logical 1.</p>
        """
        pass
    def on(self):
        """
        <h3>machine - Signal.on()</h3><p>Activate signal.</p>
        """
        pass
    def off(self):
        """
        <h3>machine - Signal.off()</h3><p>Deactivate signal.</p>
        """
        pass
class SPI:
    def __init__(self, id):
        """
        <h3>machine - SPI(id, ...)</h3><p>Construct an SPI object on the given bus, <em>id</em>. Values of <em>id</em> depend on a particular port and its hardware. Values 0, 1, etc. are commonly used to select hardware SPI block #0, #1, etc.</p><p>With no additional parameters, the SPI object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See <code>init</code> for parameters of initialisation.</p>
        """
        pass
    def init(self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK,MOSI,MISO)):
        """
        <h3>machine - SPI.init(baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))</h3><p>Initialise the SPI bus with the given parameters:</p><div><ul><li><code>baudrate</code> is the SCK clock rate.</li><li><code>polarity</code> can be 0 or 1, and is the level the idle clock line sits at.</li><li><code>phase</code> can be 0 or 1 to sample data on the first or second clock edge respectively.</li><li><code>bits</code> is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.</li><li><code>firstbit</code> can be <code>SPI.MSB</code> or <code>SPI.LSB</code>.</li><li><code>sck</code>, <code>mosi</code>, <code>miso</code> are pins (machine.Pin) objects to use for bus signals. For most hardware SPI blocks (as selected by <code>id</code> parameter to the constructor), pins are fixed and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver (<code>id</code> = -1).</li><li><code>pins</code> - WiPy port doesn’t <code>sck</code>, <code>mosi</code>, <code>miso</code> arguments, and instead allows to specify them as a tuple of <code>pins</code> parameter.</li></ul></div><p>In the case of hardware SPI the actual clock frequency may be lower than the requested baudrate. This is dependent on the platform hardware. The actual rate may be determined by printing the SPI object.</p>
        """
        pass
    def deinit(self):
        """
        <h3>machine - SPI.deinit()</h3><p>Turn off the SPI bus.</p>
        """
        pass
    def read(self, nbytes, write=0x00):
        """
        <h3>machine - SPI.read(nbytes, write=0x00)</h3><p>Read a number of bytes specified by <code>nbytes</code> while continuously writing the single byte given by <code>write</code>. Returns a <code>bytes</code> object with the data that was read.</p>
        """
        pass
    def readinto(self, buf, write=0x00):
        """
        <h3>machine - SPI.readinto(buf, write=0x00)</h3><p>Read into the buffer specified by <code>buf</code> while continuously writing the single byte given by <code>write</code>. Returns <code>None</code>.</p>
        """
        pass
    def write(self, buf):
        """
        <h3>machine - SPI.write(buf)</h3><p>Write the bytes contained in <code>buf</code>. Returns <code>None</code>.</p>
        """
        pass
    def write_readinto(self, write_buf, read_buf):
        """
        <h3>machine - SPI.write_readinto(write_buf, read_buf)</h3><p>Write the bytes from <code>write_buf</code> while reading into <code>read_buf</code>. The buffers can be the same or different, but both buffers must have the same length. Returns <code>None</code>.</p>
        """
        pass
class SoftSPI:
    def __init__(self, baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None):
        """
        <h3>machine - SoftSPI(baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None)</h3><p>Construct a new software SPI object. Additional parameters must be given, usually at least <em>sck</em>, <em>mosi</em> and <em>miso</em>, and these are used to initialise the bus. See <code>SPI.init</code> for a description of the parameters.</p>
        """
        pass
class Timer:
    def __init__(self, id, /):
        """
        <h3>machine - Timer(id, /, ...)</h3><p>Construct a new timer object of the given <code>id</code>. <code>id</code> of -1 constructs a virtual timer (if supported by a board). <code>id</code> shall not be passed as a keyword argument.</p><p>See <code>init</code> for parameters of initialisation.</p>
        """
        pass
    def init(self, *, mode=Timer.PERIODIC, freq=-1, period=-1, callback=None):
        """
        <h3>machine - Timer.init(*, mode=Timer.PERIODIC, freq=-1, period=-1, callback=None)</h3><p>Initialise the timer. Example:</p><div><div><pre>def mycallback(t): pass # periodic at 1kHz tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback) # periodic with 100ms period tim.init(period=100, callback=mycallback) # one shot firing after 1000ms tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback) </pre></div></div><p>Keyword arguments:</p><div><ul><li><code>mode</code> can be one of:</p><ul><li><code>Timer.ONE_SHOT</code> - The timer runs once until the configured period of the channel expires.</li><li><code>Timer.PERIODIC</code> - The timer runs periodically at the configured frequency of the channel.</li></ul></li><li><code>freq</code> - The timer frequency, in units of Hz. The upper bound of the frequency is dependent on the port. When both the <code>freq</code> and <code>period</code> arguments are given, <code>freq</code> has a higher priority and <code>period</code> is ignored.</li><li><code>period</code> - The timer period, in milliseconds.</li><li><code>callback</code> - The callable to call upon expiration of the timer period. The callback must take one argument, which is passed the Timer object. The <code>callback</code> argument shall be specified. Otherwise an exception will occur upon timer expiration: <code>TypeError: 'NoneType' object isn't callable</code></li></ul></div>
        """
        pass
    def deinit(self):
        """
        <h3>machine - Timer.deinit()</h3><p>Deinitialises the timer. Stops the timer, and disables the timer peripheral.</p>
        """
        pass
class UART:
    def __init__(self, id):
        """
        <h3>machine - UART(id, ...)</h3><p>Construct a UART object of the given id.</p>
        """
        pass
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, \*):
        """
        <h3>machine - UART.init(baudrate=9600, bits=8, parity=None, stop=1, \*, ...)</h3><p>Initialise the UART bus with the given parameters:</p><div><ul><li><em>baudrate</em> is the clock rate.</li><li><em>bits</em> is the number of bits per character, 7, 8 or 9.</li><li><em>parity</em> is the parity, <code>None</code>, 0 (even) or 1 (odd).</li><li><em>stop</em> is the number of stop bits, 1 or 2.</li></ul></div><p>Additional keyword-only parameters that may be supported by a port are:</p><div><ul><li><em>tx</em> specifies the TX pin to use.</li><li><em>rx</em> specifies the RX pin to use.</li><li><em>rts</em> specifies the RTS (output) pin to use for hardware receive flow control.</li><li><em>cts</em> specifies the CTS (input) pin to use for hardware transmit flow control.</li><li><em>txbuf</em> specifies the length in characters of the TX buffer.</li><li><em>rxbuf</em> specifies the length in characters of the RX buffer.</li><li><em>timeout</em> specifies the time to wait for the first character (in ms).</li><li><em>timeout_char</em> specifies the time to wait between characters (in ms).</li><li><em>invert</em> specifies which lines to invert.</p><div><ul><li><code>0</code> will not invert lines (idle state of both lines is logic high).</li><li><code>UART.INV_TX</code> will invert TX line (idle state of TX line now logic low).</li><li><code>UART.INV_RX</code> will invert RX line (idle state of RX line now logic low).</li><li><code>UART.INV_TX | UART.INV_RX</code> will invert both lines (idle state at logic low).</li></ul></div></li><li><em>flow</em> specifies which hardware flow control signals to use. The value is a bitmask.</p><div><ul><li><code>0</code> will ignore hardware flow control signals.</li><li><code>UART.RTS</code> will enable receive flow control by using the RTS output pin to signal if the receive FIFO has sufficient space to accept more data.</li><li><code>UART.CTS</code> will enable transmit flow control by pausing transmission when the CTS input pin signals that the receiver is running low on buffer space.</li><li><code>UART.RTS | UART.CTS</code> will enable both, for full hardware flow control.</li></ul></div></li></ul></div><div><p>Note</p><p>It is possible to call <code>init()</code> multiple times on the same object in order to reconfigure UART on the fly. That allows using single UART peripheral to serve different devices attached to different GPIO pins. Only one device can be served at a time in that case. Also do not call <code>deinit()</code> as it will prevent calling <code>init()</code> again.</p></div>
        """
        pass
    def deinit(self):
        """
        <h3>machine - UART.deinit()</h3><p>Turn off the UART bus.</p><div><p>Note</p><p>You will not be able to call <code>init()</code> on the object after <code>deinit()</code>. A new instance needs to be created in that case.</p></div>
        """
        pass
    def any(self):
        """
        <h3>machine - UART.any()</h3><p>Returns an integer counting the number of characters that can be read without blocking. It will return 0 if there are no characters available and a positive number if there are characters. The method may return 1 even if there is more than one character available for reading.</p><p>For more sophisticated querying of available characters use select.poll:</p><div><div><pre>poll = select.poll() poll.register(uart, select.POLLIN) poll.poll(timeout) </pre></div></div>
        """
        pass
    def read(self, nbytes):
        """
        <h3>machine - UART.read([nbytes])</h3><p>Read characters. If <code>nbytes</code> is specified then read at most that many bytes, otherwise read as much data as possible.</p><p>Return value: a bytes object containing the bytes read in. Returns <code>None</code> on timeout.</p>
        """
        pass
    def readinto(self, buf, nbytes):
        """
        <h3>machine - UART.readinto(buf [ , nbytes])</h3><p>Read bytes into the <code>buf</code>. If <code>nbytes</code> is specified then read at most that many bytes. Otherwise, read at most <code>len(buf)</code> bytes.</p><p>Return value: number of bytes read and stored into <code>buf</code> or <code>None</code> on timeout.</p>
        """
        pass
    def readline(self):
        """
        <h3>machine - UART.readline()</h3><p>Read a line, ending in a newline character.</p><p>Return value: the line read or <code>None</code> on timeout.</p>
        """
        pass
    def write(self, buf):
        """
        <h3>machine - UART.write(buf)</h3><p>Write the buffer of bytes to the bus.</p><p>Return value: number of bytes written or <code>None</code> on timeout.</p>
        """
        pass
    def sendbreak(self):
        """
        <h3>machine - UART.sendbreak()</h3><p>Send a break condition on the bus. This drives the bus low for a duration longer than required for a normal transmission of a character.</p>
        """
        pass
    def flush(self):
        """
        <h3>machine - UART.flush()</h3><p>Waits until all data has been sent. In case of a timeout, an exception is raised. The timeout duration depends on the tx buffer size and the baud rate. Unless flow control is enabled, a timeout should not occur.</p><div><p>Note</p><p>For the esp8266 and nrf ports the call returns while the last byte is sent. If required, a one character wait time has to be added in the calling script.</p></div><p>Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra</p>
        """
        pass
    def txdone(self):
        """
        <h3>machine - UART.txdone()</h3><p>Tells whether all data has been sent or no data transfer is happening. In this case, it returns <code>True</code>. If a data transmission is ongoing it returns <code>False</code>.</p><div><p>Note</p><p>For the esp8266 and nrf ports the call may return <code>True</code> even if the last byte of a transfer is still being sent. If required, a one character wait time has to be added in the calling script.</p></div><p>Availability: rp2, esp32, esp8266, mimxrt, cc3200, stm32, nrf ports, renesas-ra</p>
        """
        pass
    def irq(self, handler=None, trigger=0, hard=False):
        """
        <h3>machine - UART.irq(handler=None, trigger=0, hard=False)</h3><p>Configure an interrupt handler to be called when a UART event occurs.</p><p>The arguments are:</p><div><ul><li><em>handler</em> is an optional function to be called when the interrupt event triggers. The handler must take exactly one argument which is the <code>UART</code> instance.</li><li><em>trigger</em> configures the event(s) which can generate an interrupt. Possible values are a mask of one or more of the following:</p><ul><li><code>UART.IRQ_RXIDLE</code> interrupt after receiving at least one character and then the RX line goes idle.</li><li><code>UART.IRQ_RX</code> interrupt after each received character.</li><li><code>UART.IRQ_TXIDLE</code> interrupt after or while the last character(s) of a message are or have been sent.</li><li><code>UART.IRQ_BREAK</code> interrupt when a break state is detected at RX</li></ul></li><li><em>hard</em> if true a hardware interrupt is used. This reduces the delay between the pin change and the handler being called. Hard interrupt handlers may not allocate memory; see Writing interrupt handlers.</li></ul></div><p>Returns an irq object.</p><p>Due to limitations of the hardware not all trigger events are available on all ports.</p><table id="id1"><caption>Availability of triggers</caption><thead><tr><th><p>Port / Trigger</p></th><th><p>IRQ_RXIDLE</p></th><th><p>IRQ_RX</p></th><th><p>IRQ_TXIDLE</p></th><th><p>IRQ_BREAK</p></th></tr></thead><tbody><tr><td><p>CC3200</p></td><td></td><td><p>yes</p></td><td></td><td></td></tr><tr><td><p>ESP32</p></td><td><p>yes</p></td><td><p>yes</p></td><td></td><td><p>yes</p></td></tr><tr><td><p>MIMXRT</p></td><td><p>yes</p></td><td></td><td><p>yes</p></td><td></td></tr><tr><td><p>NRF</p></td><td></td><td><p>yes</p></td><td><p>yes</p></td><td></td></tr><tr><td><p>RENESAS-RA</p></td><td><p>yes</p></td><td><p>yes</p></td><td></td><td></td></tr><tr><td><p>RP2</p></td><td><p>yes</p></td><td></td><td><p>yes</p></td><td><p>yes</p></td></tr><tr><td><p>SAMD</p></td><td><p>yes</p></td><td><p>yes</p></td><td><p>yes</p></td><td></td></tr><tr><td><p>STM32</p></td><td><p>yes</p></td><td><p>yes</p></td><td></td><td></td></tr></tbody></table><div><p>Note</p><ul><li>The ESP32 port does not support the option hard=True.</li><li>The rp2 port’s UART.IRQ_TXIDLE is only triggered when the message is longer than 5 characters and the trigger happens when still 5 characters are to be sent.</li><li>The rp2 port’s UART.IRQ_BREAK needs receiving valid characters for triggering again.</li><li>The SAMD port’s UART.IRQ_TXIDLE is triggered while the last character is sent.</li><li>On STM32F4xx MCU’s, using the trigger UART.IRQ_RXIDLE the handler will be called once after the first character and then after the end of the message, when the line is idle.</li></ul></div><p>Availability: cc3200, esp32, mimxrt, nrf, renesas-ra, rp2, samd, stm32.</p>
        """
        pass
class WDT:
    def __init__(self, id=0, timeout=5000):
        """
        <h3>machine - WDT(id=0, timeout=5000)</h3><p>Create a WDT object and start it. The timeout must be given in milliseconds. Once it is running the timeout cannot be changed and the WDT cannot be stopped either.</p><p>Notes: On the esp8266 a timeout cannot be specified, it is determined by the underlying system. On rp2040 devices, the maximum timeout is 8388 ms.</p>
        """
        pass
    def feed(self):
        """
        <h3>machine - WDT.feed()</h3><p>Feed the WDT to prevent it from resetting the system. The application should place this call in a sensible place ensuring that the WDT is only fed after verifying that everything is functioning correctly.</p>
        """
        pass
