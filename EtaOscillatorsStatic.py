from manim import *
import numpy as np

class EtaOscillatorsStatic(Scene):
    def construct(self):
        # Parameters
        sigma = 1 # Real part
        N = 10 # Total terms
        t = 9.06472028 # Imaginary part
        scale = 2 # Zoom scale of the oscillators (so they stays within the screen)
        
        self.camera.background_color = WHITE # White background

        color_odd = RED # Odd and even branch colors
        color_even = BLUE

        origin = ORIGIN # Coordinate origin

        # Circles group
        circles_odd = VGroup()
        dots_odd = VGroup()
        arrows_odd = VGroup()
        labels_odd = VGroup()

        circles_even = VGroup()
        dots_even = VGroup()
        arrows_even = VGroup()
        labels_even = VGroup()

        # Tip positions
        tip_positions_odd = [origin]
        tip_positions_even = [origin]

        # Create terms
        for idx, n in enumerate(range(1, N+1, 2)):
            r = 1 / n**sigma * scale
            phase = -t * np.log(n)
            vec = r * np.exp(1j * phase)
            vec = np.array([vec.real, vec.imag, 0])
            center = tip_positions_odd[-1]

            circle = Circle(radius=r, stroke_color=color_odd, stroke_width=2).move_to(center)
            dot = Dot(point=center + vec, radius=0.03, color=color_odd)
            arrow = Arrow(start=center, end=center + vec, buff=0, stroke_width=2, color=color_odd)

            circles_odd.add(circle)
            dots_odd.add(dot)
            arrows_odd.add(arrow)

            tip_positions_odd.append(center + vec)

        for idx, n in enumerate(range(2, N+1, 2)):
            r = 1 / n**sigma * scale
            phase = -t * np.log(n)
            vec = r * np.exp(1j * phase)
            vec = np.array([vec.real, vec.imag, 0])
            center = tip_positions_even[-1]

            circle = Circle(radius=r, stroke_color=color_even, stroke_width=2).move_to(center)
            dot = Dot(point=center + vec, radius=0.03, color=color_even)
            arrow = Arrow(start=center, end=center + vec, buff=0, stroke_width=2, color=color_even)

            circles_even.add(circle)
            dots_even.add(dot)
            arrows_even.add(arrow)

            tip_positions_even.append(center + vec)

        # Partial sum dots (Particles)
        suma_odd_dot = Dot(point=tip_positions_odd[-1], radius=0.05, color=GREEN)
        suma_even_dot = Dot(point=tip_positions_even[-1], radius=0.05, color=GREEN)

        # Velocity values
        def velocity(n_values):
            v = np.array([0.0, 0.0, 0.0])
            for n in n_values:
                r = 1 / n**sigma * scale
                phase = -t * np.log(n)
                term = -1j * np.log(n) * r * np.exp(1j * phase)
                v += np.array([term.real, term.imag, 0.0])
            return v

        vel_odd = velocity(range(1, N+1, 2))
        vel_even = velocity(range(2, N+1, 2))

        # Velocity arrows
        velocity_arrow_scale = 0.25 # Arrow scaling (so they stays within the screen)
        velocity_arrow_odd = Arrow(
            start=suma_odd_dot.get_center(),
            end=suma_odd_dot.get_center() + vel_odd * velocity_arrow_scale,
            buff=0,
            stroke_width=3,
            color=GRAY
        )

        velocity_arrow_even = Arrow(
            start=suma_even_dot.get_center(),
            end=suma_even_dot.get_center() + vel_even * velocity_arrow_scale,
            buff=0,
            stroke_width=3,
            color=GRAY
        )

        # Add objects to scene
        self.add(
            circles_odd, dots_odd, arrows_odd, labels_odd,
            circles_even, dots_even, arrows_even, labels_even,
            suma_odd_dot, suma_even_dot,
            velocity_arrow_odd, velocity_arrow_even
        )
