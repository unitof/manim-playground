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
        vector_label1 = MathTex("\\vec{a}", color=BLUE).next_to(vector1.get_end(), UP)
        vector_label2 = MathTex("\\vec{b}", color=RED).next_to(vector2.get_end(), UP)
        
        self.play(GrowArrow(vector1), Write(vector_label1))
        self.play(GrowArrow(vector2), Write(vector_label2))
        self.wait(2)

        # Dot Product Explanation
        dot_product_explain = Text("Dot Product of Vectors", font_size=36).to_edge(UP)
        self.play(Write(dot_product_explain))
        self.wait(2)

        # Adjusting vector positions to make space for the formula
        self.play(
            vector1.animate.shift(DOWN),
            vector_label1.animate.next_to(vector1.get_end(), UP),
            vector2.animate.shift(DOWN),
            vector_label2.animate.next_to(vector2.get_end(), UP)
        )
        self.wait(2)

        # Dot Product Formula
        dot_formula = MathTex("\\vec{a} \\cdot \\vec{b} = |\\vec{a}| |\\vec{b}| \\cos(\\theta)")
        self.play(Write(dot_formula))
        self.wait(2)

        # Calculating Dot Product
        dot_calc = MathTex("\\vec{a} \\cdot \\vec{b} = 2\\times3 + 2\\times1 = 8")
        self.play(Transform(dot_formula, dot_calc))
        self.wait(2)
        
        # Fade out the dot product calculation
        self.play(FadeOut(dot_formula, shift=DOWN))
        
        # Cross Product Explanation
        cross_product_explain = Text("Cross Product of Vectors", font_size=36).to_edge(UP)
        self.play(Transform(dot_product_explain, cross_product_explain))
        self.wait(2)

        # Cross Product Formula
        cross_formula = MathTex("\\vec{a} \\times \\vec{b} = (a_2b_3-a_3b_2)\\hat{i} - (a_1b_3-a_3b_1)\\hat{j} + (a_1b_2-a_2b_1)\\hat{k}")
        self.play(Write(cross_formula))
        self.wait(2)

        # Example of Cross Product
        cross_example = MathTex("\\vec{a} \\times \\vec{b} = 0\\hat{i} - 0\\hat{j} + (2\\times1-2\\times3)\\hat{k} = -4\\hat{k}")
        self.play(Transform(cross_formula, cross_example))
        self.wait(2)

        # Conclusion and Outro
        conclusion = Text("This is a basic introduction to vector multiplication.", font_size=36)
        outro = Text("Thank you for watching!", font_size=48)
        
        # Display conclusion and outro
        self.play(Write(conclusion))
        self.wait(3)
        self.play(Transform(conclusion, outro))
        self.wait(2)

        # Fade everything out
        self.play(FadeOut(conclusion))

# Render the scene
if __name__ == "__main__":
    scene = VectorMultiplication()
    scene.render()
