from bokeh.plotting import figure, show
from bokeh.models import HoverTool, Select, CustomJS
from bokeh.layouts import column

class DataVisualizer:
    def __init__(self, training_df, ideal_df, test_df, mapping_df, best_functions, mapped_points):
        self.training_df = training_df
        self.ideal_df = ideal_df
        self.test_df = test_df
        self.mapping_df = mapping_df
        self.best_functions = best_functions
        self.mapped_points = mapped_points
        """ 
        Code for Providing Training functions
        """
        self.training_y1 = None
        self.training_y2 = None
        self.training_y3 = None
        self.training_y4 = None
        """
        Code for Providing Ideal functions
        """
        self.ideal_y13 = None
        self.ideal_y24 = None
        self.ideal_y36 = None
        self.ideal_y40 = None

        """
        Code for test and mapped functions
        """
        self.test_renderer = None
        self.mapped_renderer = None
    def create_figure(self):
        self.plot = figure(title="Training & Ideal Function Visualization", x_axis_label="X Values", y_axis_label="Y Values", width = 1200, height = 750)
        hover = HoverTool(tooltips=[ ("X Value", "$x"), ("Y Value", "$y")])
        self.plot.add_tools(hover)
        self.dropdown = Select(title="Visualization", value="All Data", options=["All Data", "Training Functions", "Chosen Ideal Functions", "Test Data", "Mapped Test Points", "Compare y1 ↔ y13", "Compare y2 ↔ y24", "Compare y3 ↔ y36", "Compare y4 ↔ y40"])
    def plot_training_functions(self):
        self.training_y1 = self.plot.line(self.training_df["x"], self.training_df["y1"], line_color = "blue", line_width=2, legend_label="Training Function y1")
        self.training_y2 = self.plot.line(self.training_df["x"], self.training_df["y2"], line_color = "green", line_width=2, legend_label="Training Function y2")
        self.training_y3 = self.plot.line(self.training_df["x"], self.training_df["y3"], line_color = "orange", line_width=2, legend_label="Training Function y3")
        self.training_y4 = self.plot.line(self.training_df["x"], self.training_df["y4"], line_color = "purple", line_width=2, legend_label="Training Function y4")
    def plot_chosen_ideal_functions(self):
        self.ideal_y13 = self.plot.line(self.ideal_df["x"], self.ideal_df["y13"], line_color = "red", line_dash="dashed", line_width=2, legend_label="Chosen Ideal Function y13")
        self.ideal_y24 = self.plot.line(self.ideal_df["x"], self.ideal_df["y24"], line_color = "brown", line_dash="dashed", line_width=2, legend_label="Chosen Ideal Function y24")
        self.ideal_y36 = self.plot.line(self.ideal_df["x"], self.ideal_df["y36"], line_color = "magenta", line_dash="dashed", line_width=2, legend_label="Chosen Ideal Function y36")
        self.ideal_y40 = self.plot.line(self.ideal_df["x"], self.ideal_df["y40"], line_color = "black", line_dash="dashed", line_width=2, legend_label="Chosen Ideal Function y40")
    def plot_test_data(self):
        self.test_renderer = self.plot.scatter(self.test_df["x"], self.test_df["y"], marker="circle", size=6, color="darkcyan", legend_label="Test Data")
    def plot_mapped_points(self):
        x_values = []
        y_values = []
        for point in self.mapped_points:
            x_values.append(point["x"])
            y_values.append(point["y"])
        self.mapped_renderer = self.plot.scatter(x_values, y_values, marker="diamond", size = 25, color="yellow", line_color = "gold", legend_label="Mapped Test Points")
    def setup_dropdown(self):
        callback = CustomJS(args=dict(dropdown=self.dropdown, ty1=self.training_y1, ty2=self.training_y2, ty3=self.training_y3, ty4=self.training_y4, iy13=self.ideal_y13, iy24=self.ideal_y24, iy36=self.ideal_y36, iy40=self.ideal_y40, test=self.test_renderer, mapped=self.mapped_renderer),




            code = """

               // Hiding first thing everywhere
const renderers = [ty1, ty2, ty3, ty4, iy13, iy24, iy36, iy40, test, mapped];
                    for (let i = 0; i < renderers.length; i++) 
                    {renderers[i].visible = false;}
               // Current dropdown selection
               const option = cb_obj.value;
               // ----------------------------
               // ALL of the data
               // ----------------------------
               if(option == "All Data")
               {ty1.visible = true; ty2.visible = true; ty3.visible = true; ty4.visible = true; iy13.visible = true; iy24.visible = true; iy36.visible = true; iy40.visible = true; test.visible = true; mapped.visible = true;}
               // ----------------------------
               // All of the training functions
               // ----------------------------
               else if(option == "Training Functions")
               {ty1.visible = true; ty2.visible = true; ty3.visible = true; ty4.visible = true;}
               // ----------------------------
               // All the Ideal Functions
               // ----------------------------
               else if(option == "Chosen Ideal Functions")
               {iy13.visible = true; iy24.visible = true; iy36.visible = true; iy40.visible = true;}
               // ----------------------------
               // All of the Test Data
               // ----------------------------
               else if(option == "Test Data")
               {test.visible = true;}
               // ----------------------------
               // All of the Mapped Test Points
               // ----------------------------
               else if (option == "Mapped Test Points") 
               {mapped.visible = true;}
// =========================
// Comparing y1 ↔ y13
// =========================
else if (option == "Compare y1 ↔ y13") 
{ty1.visible = true; iy13.visible = true;}
// =========================
// Comparing y2 ↔ y24
// =========================
else if (option == "Compare y2 ↔ y24") 
{ty2.visible = true; iy24.visible = true;}
// =========================
// Comparing y3 ↔ y36
// =========================
else if (option == "Compare y3 ↔ y36") 
{ty3.visible = true; iy36.visible = true;}
// =========================
// Comparing y4 ↔ y40
// =========================
else if (option == "Compare y4 ↔ y40") 
{ty4.visible = true; iy40.visible = true;}""")
        self.dropdown.js_on_change("value", callback)
    def show_visualization(self):
        layout = column(self.dropdown, self.plot)
        show(layout)