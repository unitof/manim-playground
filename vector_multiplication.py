from manim import *

class VectorMultiplication(Scene):
    def construct(self):
        # Introduction
        title = Text("Vector Multiplication", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Section 1: Introduction to Vectors
        intro_vectors = Text("Let's start with the basics of vectors.", font_size=36)
        self.play(Write(intro_vectors))
        self.wait(2)
        self.play(FadeOut(intro_vectors))
        
        # Displaying vectors
        vector1 = Arrow(ORIGIN, [2, 2, 0], buff=0, color=BLUE)
        vector2 = Arrow(ORIGIN, [3, 1, 0], buff=0, color=RED)
        vector_label1 = MathTex("\\vec{a}", color=BLUE).next_to(vector1, RIGHT)
        vector_label2 = MathTex("\\vec{b}", color=RED).next_to(vector2, RIGHT)
        
        self.play(GrowArrow(vector1), Write(vector_label1))
        self.play(GrowArrow(vector2), Write(vector_label2))
        self.wait(2)

        # Dot Product
        dot_product_explain = Text("Dot Product of Vectors", font_size=36).to_edge(UP)
        self.play(ReplacementTransform(vector_label1, dot_product_explain))
        self.wait(2)

        self.play(
            vector1.animate.shift(DOWN * 2),
            vector2.animate.shift(DOWN * 2),
            vector_label1.animate.next_to(vector1, RIGHT),
            vector_label2.animate.next_to(vector2, RIGHT)
        )

        dot_formula = MathTex("\\vec{a} \\cdot \\vec{b} = |\\vec{a}| |\\vec{b}| \\cos(\\theta)")
        self.play(Write(dot_formula))
        self.wait(2)

        # Calculating Dot Product
        dot_calc = MathTex("\\vec{a} \\cdot \\vec{b} = 2\\times3 + 2\\times1 = 8")
        self.play(Transform(dot_formula, dot_calc))
        self.wait(2)
        
        self.play(FadeOut(dot_formula, shift=DOWN))
        
        # Cross Product
        cross_product_explain = Text("Cross Product of Vectors", font_size=36)
        self.play(Write(cross_product_explain))
        self.wait(2)

        cross_formula = MathTex("\\vec{a} \\times \\vec{b} = (a_2b_3-a_3b_2)\\hat{i} - (a_1b_3-a_3b_1)\\hat{j} + (a_1b_2-a_2b_1)\\hat{k}")
        self.play(Write(cross_formula))
        self.wait(2)

        # Example of Cross Product
        cross_example = MathTex("\\vec{a} \\times \\vec{b} = 0\\hat{i} - 0\\hat{j} + (2\\times1-2\\times3)\\hat{k} = -4\\hat{k}")
        self.play(Transform(cross_formula, cross_example))
        self.wait(2)

        self.play(FadeOut(cross_formula), FadeOut(cross_product_explain))
        self.wait(1)

        # Conclusion
        conclusion = Text("This is a basic introduction to vector multiplication.", font_size=36)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))

        # Outro
        outro = Text("Thank you for watching!", font_size=48)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))

# Render the scene
if __name__ == "__main__":
    scene = VectorMultiplication()
    scene.render()
