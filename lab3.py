#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: lab3
# GNU Radio version: 3.9.5.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
import bokehgui
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx




class lab3(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "lab3", catch_exceptions=True)
        self.plot_lst = []
        self.widget_lst = []

        ##################################################
        # Variables
        ##################################################
        self.signal_amp = signal_amp = 5
        self.samp_rate = samp_rate = 32000
        self.noise_amp = noise_amp = 0.01
        self.frequency = frequency = 100

        ##################################################
        # Blocks
        ##################################################
        self.signal_amp_slider = bokehgui.slider(self.widget_lst, 'Signal Amplitude' +":", 0, 10, 0.01, 1, 5)
        self.signal_amp_slider.add_callback(lambda attr, old, new: self.set_signal_amp(new))
        self.noise_amp_slider = bokehgui.slider(self.widget_lst, 'Noise Amplidude' +":", 0.01, 10, 0.01, 1, 0.01)
        self.noise_amp_slider.add_callback(lambda attr, old, new: self.set_noise_amp(new))
        self.frequency_slider = bokehgui.slider(self.widget_lst, 'Frequency' +":", 10, 10000, 1, 1, 100)
        self.frequency_slider.add_callback(lambda attr, old, new: self.set_frequency(new))
        self.bokehgui_time_sink_x_0 = bokehgui.time_sink_f_proc(1024, samp_rate, "",
         1
        )


        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        legend_list = []
        for i in  range(    1  ):
          if len(labels[i]) == 0:
            legend_list.append("Data {0}".format(i))
          else:
            legend_list.append(labels[i])

        self.bokehgui_time_sink_x_0_plot = bokehgui.time_sink_f(self.plot_lst, self.bokehgui_time_sink_x_0, log_x = False, log_y = False, update_time = 100, legend_list = legend_list, is_message =   False)

        self.bokehgui_time_sink_x_0_plot.set_y_axis([-1, 1])
        self.bokehgui_time_sink_x_0_plot.set_y_label('Amplitude' + '(' +""+')')
        self.bokehgui_time_sink_x_0_plot.set_x_label('Time' + '(' +""+')')

        self.bokehgui_time_sink_x_0_plot.enable_tags(-1, True)
        self.bokehgui_time_sink_x_0_plot.set_trigger_mode(bokehgui.TRIG_MODE_FREE, bokehgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.bokehgui_time_sink_x_0_plot.enable_grid(False)
        self.bokehgui_time_sink_x_0_plot.enable_axis_labels(True)
        self.bokehgui_time_sink_x_0_plot.enable_legend(True)
        self.bokehgui_time_sink_x_0_plot.set_layout(*((1,0)))

        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "blue", "blue", "blue"]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        styles = ["solid", "solid", "solid", "solid", "solid",
                  "solid", "solid", "solid", "solid", "solid"]
        markers = [None, None, None, None, None,
                  None, None, None, None, None]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in  range(     1  ):
          self.bokehgui_time_sink_x_0_plot.format_line(i, colors[i], widths[i], styles[i], markers[i], alphas[i])
        self.bokehgui_frequency_sink_x_0 = bokehgui.freq_sink_f_proc(1024,
                             window.WIN_BLACKMAN_hARRIS,
                             0, samp_rate,
                             "",                     1                    )

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        legend_list = []

        for i in  range(1):
            if len(labels[i]) == 0:
                legend_list.append("Data {0}".format(i))
            else:
                legend_list.append(labels[i])

        self.bokehgui_frequency_sink_x_0_plot = bokehgui.freq_sink_f(self.plot_lst, self.bokehgui_frequency_sink_x_0, update_time = 100, legend_list = legend_list, is_message =False)

        self.bokehgui_frequency_sink_x_0_plot.set_y_axis([-140, 10])
        self.bokehgui_frequency_sink_x_0_plot.set_y_label('Relative Gain' + '(' +'dB'+')')
        self.bokehgui_frequency_sink_x_0_plot.set_x_label('Frequency' + '(' +""+')')

        self.bokehgui_frequency_sink_x_0_plot.set_trigger_mode(bokehgui.TRIG_MODE_FREE,0.0, 0, "")

        self.bokehgui_frequency_sink_x_0_plot.enable_grid(False)
        self.bokehgui_frequency_sink_x_0_plot.enable_axis_labels(True)
        self.bokehgui_frequency_sink_x_0_plot.enable_legend(True)
        self.bokehgui_frequency_sink_x_0_plot.set_plot_pos_half(False)
        self.bokehgui_frequency_sink_x_0_plot.set_layout(*((0,1,2,1)))
        self.bokehgui_frequency_sink_x_0_plot.enable_max_hold()
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        styles = ["solid", "solid", "solid", "solid", "solid",
                  "solid", "solid", "solid", "solid", "solid"]
        markers = [None, None, None, None, None,
                   None, None, None, None, None]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in  range(1):
            self.bokehgui_frequency_sink_x_0_plot.format_line(i, colors[i], widths[i], styles[i], markers[i], alphas[i])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frequency, signal_amp, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.bokehgui_frequency_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.bokehgui_time_sink_x_0, 0))


    def get_signal_amp(self):
        return self.signal_amp

    def set_signal_amp(self, signal_amp):
        self.signal_amp = signal_amp
        self.analog_sig_source_x_0.set_amplitude(self.signal_amp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.bokehgui_frequency_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.bokehgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency(self.frequency)




def main(top_block_cls=lab3, options=None):
    # Create Top Block instance
    tb = top_block_cls()

    try:
        tb.start()

        bokehgui.utils.run_server(tb, sizing_mode = "fixed",  widget_placement =  (0, 0), window_size =  (768, 1366))
    finally:
        print("Exiting the simulation. Stopping Bokeh Server")
        tb.stop()
        tb.wait()


if __name__ == '__main__':
    main()
