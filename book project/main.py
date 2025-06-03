from tkinter import *
from tkinter import messagebox
import random

def show_checkout_screen(selected_books):

    checkout_root = Toplevel(root)
    checkout_root.geometry("500x500")
    checkout_root.title("Checkout")

    Label(checkout_root, text="Order Summary", font=("Arial", 16, "bold")).pack(pady=10)

    total_price = 0
    tax_rate = 0.08
    shipping_cost = 5.99
    for book_name, quantity in selected_books:
        price = round(random.uniform(10.00, 50.00), 2)
        taxes = round(price * tax_rate, 2)
        subtotal = round((price + taxes) * quantity, 2)
        total_price += subtotal
        frame = Frame(checkout_root)
        frame.pack(pady=5)
        Label(frame, image=book_data[book_name]["image"]).grid(row=0, column=0, rowspan=3)
        Label(frame, text=f"Book: {book_name}", font=("Arial", 12)).grid(row=0, column=1, sticky="w", padx=10)
        Label(frame, text=f"Quantity: {quantity}", font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=10)
        Label(frame, text=f"Price: ${price:.2f} ea | Taxes: ${taxes:.2f} ea", font=("Arial", 10)).grid(row=2, column=1, sticky="w", padx=10)
        Label(frame, text=f"Subtotal: ${subtotal:.2f}", font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w", padx=10)

    total_price = round(total_price + shipping_cost, 2)
    Label(checkout_root, text=f"Shipping/Handling: ${shipping_cost:.2f}", font=("Arial", 12)).pack(pady=5)
    Label(checkout_root, text=f"Total: ${total_price:.2f}", font=("Arial", 14, "bold")).pack(pady=10)

    def place_order():
        summary = "\n".join([f"{name} (x{qty})" for name, qty in selected_books])
        messagebox.showinfo("Order Confirmation", f"Your order for:\n{summary}\nhas been placed successfully!")
        checkout_root.destroy()
        root.destroy()

    Button(checkout_root, text="Place Order", command=place_order, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=20)


def select_book(book_name):
    selected_book_var.set(book_name)
    for frame, name in book_frames:
        if name == book_name:
            frame.config(bg="#d0eaff")
        else:
            frame.config(bg=root.cget('bg'))


def initiate_checkout():
    selected_books = [(name, quantity_vars[name].get()) for name in book_names if quantity_vars[name].get() > 0]
    if not selected_books:
        messagebox.showwarning("Selection Error", "Please select at least one book and quantity before proceeding to checkout.")
        return
    show_checkout_screen(selected_books)

root = Tk()
root.geometry("900x700")
root.title("Book Selection")

try:
    book1 = PhotoImage(file="shoeh.png")
    book2 = PhotoImage(file="hsl.png")
    book3 = PhotoImage(file="lnattc.png")
    book4 = PhotoImage(file="tkam.png")
    book5 = PhotoImage(file="trok.png")
    book6 = PhotoImage(file="tsok.png")
except TclError as e:
    messagebox.showerror("Image Error", f"Could not load image files. Please ensure they are in the same directory as the script.\nError: {e}")
    root.destroy()

book_data = {
    "The Seven Husbands of Evelyn Hugo": {"image": book1},
    "Happy Sugar Life": {"image": book2},
    "Last Night at the Telegraph Club": {"image": book3},
    "To Kill a Mockingbird": {"image": book4},
    "The Rise of Kyoshi": {"image": book5},
    "The Shadow of Kyoshi": {"image": book6},
}

book_names = list(book_data.keys())

selected_book_var = StringVar(value=book_names[0] if book_names else "")

label1 = Label(root, text="Choose a Book", font=("Arial", 16, "bold"))
label1.pack(pady=10)

book_frames = []
quantity_vars = {}

books_frame = Frame(root)
books_frame.pack(pady=10)

num_columns = 2  
for idx, book_name in enumerate(book_names):
    row = idx // num_columns
    col = idx % num_columns
    frame = Frame(books_frame, bd=2, relief=RIDGE, padx=10, pady=10)
    frame.grid(row=row, column=col, sticky="nsew", pady=5, padx=5)
    book_frames.append((frame, book_name))
    
    img_label = Label(frame, image=book_data[book_name]["image"])
    img_label.grid(row=0, column=0, rowspan=2)
    img_label.bind("<Button-1>", lambda e, n=book_name: select_book(n))
    
    title_label = Label(frame, text=book_name, font=("Arial", 12, "bold"), cursor="hand2")
    title_label.grid(row=0, column=1, sticky="w", padx=10)
    title_label.bind("<Button-1>", lambda e, n=book_name: select_book(n))
    
    quantity_vars[book_name] = IntVar(value=0)
    qty_label = Label(frame, text="Quantity:")
    qty_label.grid(row=1, column=1, sticky="w", padx=10)
    qty_spin = Spinbox(frame, from_=0, to=99, width=5, textvariable=quantity_vars[book_name])
    qty_spin.grid(row=1, column=2, sticky="w")

checkout_button = Button(
    root,
    text="Continue to Checkout",
    command=initiate_checkout,
    bg="blue",
    fg="white",
    font=("Arial", 14, "bold")
)
checkout_button.pack(pady=20)

root.mainloop()
