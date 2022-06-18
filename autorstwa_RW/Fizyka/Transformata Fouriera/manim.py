import scipy
import scipy.fftpack
from manim import *
import numpy as np
from numpy import fft
import math


class Something(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))


class Graph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 12, 1],
            x_length=12,
            y_range=[-1.9, 1.9, 1],
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label='x', y_label='y').set_color(WHITE)
        labels.shift(1 * DOWN)
        self.add(labels)

        axes.shift(1 * DOWN)
        x = stepRange(0, 10, 100)
        line = axes.plot_line_graph(x, f(x), add_vertex_dots=False, line_color='#FFFF00')
        line2 = axes.plot_line_graph(x, g(x), add_vertex_dots=False, line_color='#FF0000')
        self.add(axes)

        eq1 = MathTex(r"f(x)=sin(\omega x), \omega=1")
        eq1.shift(3 * UP)
        eq1.shift(3 * LEFT)
        self.play(Create(line), Write(eq1), run_time=4)

        self.wait(10)

        eq2 = MathTex(r"g(x)=\frac{1}{2}sin(\omega_1 x), \omega_1=2")
        eq2.shift(3 * UP)
        eq2.shift(3 * RIGHT)
        self.play(Create(line2), Write(eq2), run_time=4)

        eq3 = MathTex(r"s(x)=sin(\omega x)+\frac{1}{2}sin(\omega_1 x)")
        eq3.shift(3 * UP)

        eq6 = MathTex(r"f_0=\frac{1}{\pi}")
        eq6.shift(1 * LEFT)
        eq7 = MathTex(r"f_1=\frac{1}{2\pi}")
        eq7.shift(1 * RIGHT)
        eq8 = MathTex(r"\omega=2\pi f")
        eq8.shift(2 * UP)

        self.wait(5)

        line3 = axes.plot_line_graph(x, s(x), add_vertex_dots=False, line_color='#FFA500')
        self.play(Unwrite(eq1), Unwrite(eq2))
        self.play(Create(line3), Write(eq3), run_time=4)
        self.play(Uncreate(line), Uncreate(line2))
        self.play(Write(eq6), Write(eq7), Write(eq8))

        self.wait(5)


class Graph2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 1.1, 0.5],
            axis_config={"include_numbers": True}
        )
        eq4 = MathTex(r"A(f)=\int_{t_1}^{t_2}f(x)e^{-2\pi ixf}dx")
        eq4.shift(3 * UP)
        eq4.shift(1 * RIGHT)
        self.play(Write(eq4))

        self.play(Create(axes))
        labels = axes.get_axis_labels(x_label='f', y_label='A').set_color(WHITE)
        self.play(Write(labels))

        self.play(Indicate(eq4))
        eq5 = MathTex(r"A(f)=\int_{t_1}^{t_2}(sin(x)+\frac{1}{2}sin(\frac{x}{2}))e^{-2\pi ixf}dx")
        eq5.shift(3 * UP)
        eq5.shift(1 * RIGHT)
        self.play(Unwrite(eq4))
        self.play(Write(eq5))


        # Number of samplepoints
        N = 1000
        # sample spacing
        T = 1
        x = np.linspace(0.0, N * T, N)
        y = np.sin(x) + 0.5 * np.sin(2 * x)
        yf = scipy.fftpack.fft(y)
        xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

        line4 = axes.plot_line_graph(xf, 2.0 / N * np.abs(yf[:N // 2]),
                                     add_vertex_dots=False,
                                     line_color='#FFA500')

        P1 = MathTex(r"(\frac{1}{2\pi},A_0)").scale(0.75).next_to(axes.c2p(1 / (2 * np.pi), 0.9, 0))
        P2 = MathTex(r"(\frac{1}{\pi},A_1)").scale(0.75).next_to(axes.c2p(1 / np.pi, 0.4, 0))
        self.play(Create(line4), Write(P1), Write(P2), run_time=4)

        self.wait(10)


class Graph3(Scene):
    def construct(self):
        eq4 = MathTex(r"F(v)=\int_{-\infty}^{+\infty}f(x)e^{-2\pi ivx}dx")
        self.play(Write(eq4))
        self.wait(10)


def stepRange(start, finish, step):
    return [x / step for x in range(start, finish * step)]


def f(x):
    return np.sin(x)


def g(x):
    arn = []
    for v in x:
        arn.append(1 / 2 * np.sin(2 * v))
    return arn


def s(x):
    return f(x) + g(x)
