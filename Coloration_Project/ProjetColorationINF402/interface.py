import tkinter as tk
from tkinter import PhotoImage
from main import creer_Dimac_fich, solve_sat_from_dimacs_file, interprete_solution
from tkinter import messagebox
from graphes import listedegraphes
from draw import draw_colored_graph,draw_graph
from PIL import Image, ImageTk
nb = 0  # Define nb as a global variable with initial value 0

def start_application():
    # Switch to the MenuPage
    app.show_frame("MenuPage")

   # To exit 
def exit_application():
    app.quit()






class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menu_label = tk.Label(self, text="Menu Page", font=("Poppins", 24), bg="#EDF2EF", fg="#212738")
        menu_label.pack(pady=20)
        try:
            image = PhotoImage(file="graph_coloring.png")  # Change "your_photo.png" with your actual photo file
            # Resize the photo (change 2 to any other integer to scale down further)
            image = image.subsample(2)
            image_label = tk.Label(self, image=image, bg="#EDF2EF")
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.pack(pady=20)
        except tk.TclError:
            print("Image file not found or not supported")

        new_graph_button = tk.Button(self, text="Create a New Graph", command=self.create_new_graph, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        new_graph_button.pack(pady=10)

        existing_graph_button = tk.Button(self, text="Use an Existing Graph", command=self.use_existing_graph, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        existing_graph_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.go_back, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        back_button.pack(pady=10)

    def create_new_graph(self):
        # Switch to the GraphInputPage
        app.show_frame("GraphInputPage")

    def use_existing_graph(self):
        # Add functionality for using an existing graph here
        app.show_frame("ChooseGraphPage")

    def go_back(self):
        # Switch back to the StartPage
        app.show_frame("StartPage")

class FenetreTkinter:
    def __init__(self, master, graphe):
        self.graphe = graphe

        # Créer une frame pour afficher les messages
        self.frame_messages = tk.Frame(master)
        self.frame_messages.pack()

        # Créer une étiquette pour afficher les messages
        self.label_messages = tk.Label(self.frame_messages, text="")
        self.label_messages.pack()

    # Fonction pour afficher les messages
    def afficher_messages(self):
        messages = ""
        for sommet, couleur in self.graphe.items():
            message = f"Sommet {sommet} est coloré avec la couleur {couleur}.\n"
            messages += message
        self.label_messages.config(text=messages)
class ChooseGraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.solution_exists = False  # Boolean to track if a solution exists
        self.num_chosen_graph = tk.StringVar()
        self.num_chosen_graph.set("0")  # Default value
        self.nb_colors = tk.StringVar()
        self.nb_colors.set("0")  # Default value

        app_name_label = tk.Label(self, text="Graphix", font=("Poppins", 48, "bold"), bg="#EDF2EF", fg="#212738")
        app_name_label.pack(pady=20)

        exis_graph_button = tk.Button(self, text="see existing graphes", command=self.open_image_window, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        exis_graph_button.pack(pady=10)

        label = tk.Label(self, text="Enter the number of the graph you want to use [1 to 8]:", font=("Poppins", 14), bg="#EDF2EF", fg="#212738")
        label.pack(pady=10)

        self.graph_number_entry = tk.Entry(self,textvariable=self.num_chosen_graph, font=("Poppins", 12))
        self.graph_number_entry.pack(pady=5)

        colors_label = tk.Label(self, text="Enter number of your colors:", font=("Poppins", 14), bg="#EDF2EF", fg="#212738")
        colors_label.pack(pady=10)

        self.nb_colors_entry = tk.Entry(self,textvariable=self.nb_colors, font=("Poppins", 12))
        self.nb_colors_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Submit", command=self.submit_graph_number, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        submit_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.go_back, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        back_button.pack(pady=10)
    def submit_graph_number(self):
        graph_number = self.graph_number_entry.get()
        nom_graph = "graphe" + str(graph_number)
        graphe = listedegraphes[nom_graph]
        Ncolors = int(self.nb_colors_entry.get())
        colors=list(range(1, Ncolors + 1))
        creer_Dimac_fich(graphe, colors, 'existing.dimacs')

        # Solve the SAT problem from the DIMACS file
        (solution_sat, self.solution_exists) = solve_sat_from_dimacs_file("existing.dimacs")
        if self.solution_exists:
            colors_graph = interprete_solution(solution_sat, Ncolors)

            # Display the solution using FenetreTkinter
            self.display_solution(colors_graph)
            draw_graph(graphe)
            draw_colored_graph(graphe,colors_graph)
        else:
            # No solution exists, display a message
            self.display_no_solution()

    def display_solution(self, colors_graph):
        # Create a new window to display the colored graph
        fenetre_tkinter = FenetreTkinter(self, colors_graph)
        fenetre_tkinter.afficher_messages()

    def display_no_solution(self):
        # Display a message indicating that no solution exists
        messagebox.showerror("No Solution", "Il n'existe aucune coloration correcte pour ce graphe.")

    def go_back(self):
        # Switch back to the MenuPage
        app.show_frame("MenuPage")

    def open_image_window(self):
        image_window = ImageWindow(self)
        image_window.show_image("CATALOGUE-GRAPHE.png")  # Change "example_image.jpg" to your image file path


class ImageWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Image Window")

        self.label = tk.Label(self)
        self.label.pack()

    def show_image(self, image_path):
        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.label.configure(image=photo)
            self.label.image = photo
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file not found!")



class ScrolledWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Configure canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Add scrollbar and scrollable frame to canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Bind mousewheel scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_canvas_configure(self, event):
        """Update scroll region whenever canvas is resized."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        """Scroll canvas using mousewheel."""
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")


class GraphInputPage(ScrolledWindow):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.solution_exists = False  # Boolean to track if a solution exists

        self.num_vertices = tk.StringVar()
        self.num_vertices.set("0")  # Default value

        input_label = tk.Label(self.scrollable_frame, text="Enter the number of vertices:", font=("Poppins", 14), bg="#EDF2EF", fg="#212738")
        input_label.pack(pady=10)

        num_vertices_entry = tk.Entry(self.scrollable_frame, textvariable=self.num_vertices, font=("Poppins", 12))
        num_vertices_entry.pack(pady=5)

        self.neighbor_entries = []

        submit_button = tk.Button(self.scrollable_frame, text="Next", command=self.create_neighbor_entries, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        submit_button.pack(pady=10)

        back_button = tk.Button(self.scrollable_frame, text="Back", command=self.go_back, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        back_button.pack(pady=10)

    def create_neighbor_entries(self):
        num_vertices = int(self.num_vertices.get())
        for entry in self.neighbor_entries:
            entry.destroy()
        self.neighbor_entries = []
        for i in range(num_vertices):
            neighbor_label = tk.Label(self.scrollable_frame, text=f"Neighbors for Vertex {i+1}:", font=("Poppins", 12), bg="#EDF2EF", fg="#212738")
            neighbor_label.pack(pady=5)
            neighbor_entry = tk.Entry(self.scrollable_frame, font=("Poppins", 12))
            neighbor_entry.pack(pady=5)
            self.neighbor_entries.append(neighbor_entry)

        num_colors_label = tk.Label(self.scrollable_frame, text="Enter the number of colors:", font=("Poppins", 14), bg="#EDF2EF", fg="#212738")
        num_colors_label.pack(pady=10)

        self.num_colors_entry = tk.Entry(self.scrollable_frame, font=("Poppins", 12))
        self.num_colors_entry.pack(pady=5)

        submit_button = tk.Button(self.scrollable_frame, text="Submit", command=self.submit_graph, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        submit_button.pack(pady=10)

    def submit_graph(self):

        global nb  # Access the global nb variable
        num_vertices = int(self.num_vertices.get())
        nb = num_vertices  # Store the number of vertices in variable nb
        graph_data = {'graphe': [], 'nba': 0}
        edges = set()
        for i in range(num_vertices):
            neighbors = [int(x) for x in self.neighbor_entries[i].get().split()]
            graph_data['graphe'].append(neighbors)
            for neighbor in neighbors:
                # Avoid counting the same edge twice
                if (i+1, neighbor) not in edges and (neighbor, i+1) not in edges:
                    edges.add((i+1, neighbor))
        graph_data['nba'] = len(edges)
        print("Graph Data:", graph_data)

        # Get the number of colors from the entry field
        num_colors = int(self.num_colors_entry.get())
        couleurs = list(range(1, num_colors + 1))
        lenCouleurs = len(couleurs)

        # Call the creer_Dimac_fich function with the filled graph_data and the number of colors
        creer_Dimac_fich(graph_data, couleurs, 'creating.dimacs')

        # Solve the SAT problem from the DIMACS file
        (solution_sat, self.solution_exists) = solve_sat_from_dimacs_file("creating.dimacs")
        if self.solution_exists:
            colors_graph = interprete_solution(solution_sat, lenCouleurs)
            draw_graph(graph_data)
            draw_colored_graph(graph_data,colors_graph)
            # Display the solution using FenetreTkinter
            self.display_solution(colors_graph)
        else:
            # No solution exists, display a message
            self.display_no_solution()

    def display_solution(self, colors_graph):
        # Create a new window to display the colored graph
        fenetre_tkinter = FenetreTkinter(self, colors_graph)
        fenetre_tkinter.afficher_messages()

    def display_no_solution(self):
        # Display a message indicating that no solution exists
        messagebox.showerror("No Solution", "Il n'existe aucune coloration correcte pour ce graphe.")

    def go_back(self):
        # Switch back to the MenuPage
        app.show_frame("MenuPage")




class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, GraphInputPage,ChooseGraphPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welcome_label = tk.Label(self, text="Welcome to", font=("Poppins", 20), bg="#EDF2EF", fg="#212738")
        welcome_label.pack(pady=10)

        app_name_label = tk.Label(self, text="Graphix", font=("Poppins", 48, "bold"), bg="#EDF2EF", fg="#212738")
        app_name_label.pack(pady=20)

        # Add an image
        try:
            image = PhotoImage(file="graph_coloring.png")  # Change "your_photo.png" with your actual photo file
            # Resize the photo (change 2 to any other integer to scale down further)
            image = image.subsample(2)
            image_label = tk.Label(self, image=image, bg="#EDF2EF")
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.pack(pady=20)
        except tk.TclError:
            print("Image file not found or not supported")

        # Add a start button
        start_button = tk.Button(self, text="Start", command=start_application, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        start_button.config(borderwidth=0, highlightthickness=0, padx=20, pady=10)  # Increase button padding
        start_button.pack(pady=20)

        exit_button = tk.Button(self, text="Exit", command=exit_application, font=("Poppins", 12), bg="#212738", fg="#FFFFFF")
        exit_button.config(borderwidth=0, highlightthickness=0, padx=20, pady=12)  # Increase button padding
        exit_button.pack(pady=20)

if __name__ == "__main__":
    app = Application()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}")
    app.title("GraphiX")    
    app.mainloop()