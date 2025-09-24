import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import json
import time

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced QR Code Generator")
        self.root.geometry("1000x700")
        self.root.minsize(900, 650)
        self.is_dark_theme = False
        self.current_qr_image = None
        self.logo_path = None
        self.fg_color = "#000000"
        self.bg_color = "#FFFFFF"
        
        self.load_settings()
        self.setup_styles()
        self.create_widgets()
        self.apply_theme()
        self.center_window()
    
    def setup_styles(self):
        """Setup custom styles for the application"""
        self.style = ttk.Style()
        
       
        self.light_theme = {
            'bg': '#f0f0f0',
            'fg': '#333333',
            'select_bg': '#0078d4',
            'select_fg': '#ffffff',
            'entry_bg': '#ffffff',
            'entry_fg': '#000000',
            'button_bg': '#e1e1e1',
            'frame_bg': '#ffffff',
            'accent': '#0078d4'
        }
        
       
        self.dark_theme = {
            'bg': '#2d2d2d',
            'fg': '#ffffff',
            'select_bg': '#404040',
            'select_fg': '#ffffff',
            'entry_bg': '#404040',
            'entry_fg': '#ffffff',
            'button_bg': '#404040',
            'frame_bg': '#353535',
            'accent': '#00a2ed'
        }
        
        self.configure_styles()
    
    def configure_styles(self):
        """Configure ttk styles"""
        theme = self.dark_theme if self.is_dark_theme else self.light_theme
        

        self.style.configure('Custom.TNotebook', 
                           background=theme['bg'],
                           borderwidth=0)
        self.style.configure('Custom.TNotebook.Tab',
                           background=theme['button_bg'],
                           foreground=theme['fg'],
                           padding=[20, 10],
                           font=('Segoe UI', 10))
        

        self.style.configure('Custom.TFrame',
                           background=theme['frame_bg'],
                           relief='flat')
        

        self.style.configure('Custom.TLabel',
                           background=theme['frame_bg'],
                           foreground=theme['fg'],
                           font=('Segoe UI', 10))
        
        self.style.configure('Title.TLabel',
                           background=theme['frame_bg'],
                           foreground=theme['fg'],
                           font=('Segoe UI', 14, 'bold'))
        

        self.style.configure('Custom.TButton',
                           font=('Segoe UI', 10),
                           padding=[10, 8])
        

        self.style.configure('Custom.TEntry',
                           font=('Segoe UI', 10),
                           padding=[5, 5])
        

        self.style.configure('Custom.TCombobox',
                           font=('Segoe UI', 10),
                           padding=[5, 5])
    
    def create_widgets(self):

        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        

        header_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 10))
        

        title_label = ttk.Label(header_frame, text="🔲 Advanced QR Code Generator", 
                               style='Title.TLabel')
        title_label.pack(side='left')

        self.theme_btn = ttk.Button(header_frame, text="🌙 Dark Mode", 
                                   command=self.toggle_theme, style='Custom.TButton')
        self.theme_btn.pack(side='right')

        content_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        left_panel = ttk.Frame(content_frame, style='Custom.TFrame')
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.configure(width=400)

        right_panel = ttk.Frame(content_frame, style='Custom.TFrame')
        right_panel.pack(side='right', fill='both', expand=True)
        
        self.create_control_panel(left_panel)
        self.create_preview_panel(right_panel)
    
    def create_control_panel(self, parent):

        content_frame = ttk.LabelFrame(parent, text="QR Code Content", style='Custom.TFrame')
        content_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(content_frame, text="Text/URL:", style='Custom.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        
        self.text_var = tk.StringVar(value="https://muhammad-usman-ashy.vercel.app")
        self.text_entry = tk.Text(content_frame, height=3, font=('Segoe UI', 10), 
                                 wrap='word', relief='flat', padx=10, pady=8)
        self.text_entry.pack(fill='x', padx=10, pady=(0, 10))
        self.text_entry.insert('1.0', self.text_var.get())
        self.text_entry.bind('<KeyRelease>', self.on_text_change)
        
        style_frame = ttk.LabelFrame(parent, text="Style Options", style='Custom.TFrame')
        style_frame.pack(fill='x', pady=(0, 10))
        

        ttk.Label(style_frame, text="Error Correction:", style='Custom.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        self.error_correction = ttk.Combobox(style_frame, values=[
            "Low (7%)", "Medium (15%)", "Quartile (25%)", "High (30%)"
        ], state='readonly', style='Custom.TCombobox')
        self.error_correction.set("Medium (15%)")
        self.error_correction.pack(fill='x', padx=10, pady=(0, 10))
        self.error_correction.bind('<<ComboboxSelected>>', self.generate_qr)
        

        ttk.Label(style_frame, text="Module Style:", style='Custom.TLabel').pack(anchor='w', padx=10, pady=(5, 5))
        self.module_style = ttk.Combobox(style_frame, values=[
            "Square", "Rounded", "Circle"
        ], state='readonly', style='Custom.TCombobox')
        self.module_style.set("Square")
        self.module_style.pack(fill='x', padx=10, pady=(0, 10))
        self.module_style.bind('<<ComboboxSelected>>', self.generate_qr)
        

        color_frame = ttk.LabelFrame(parent, text="Color Options", style='Custom.TFrame')
        color_frame.pack(fill='x', pady=(0, 10))
        

        fg_color_frame = ttk.Frame(color_frame, style='Custom.TFrame')
        fg_color_frame.pack(fill='x', padx=10, pady=(10, 5))
        
        ttk.Label(fg_color_frame, text="Foreground Color:", style='Custom.TLabel').pack(side='left')
        self.fg_color_btn = tk.Button(fg_color_frame, text="⬛", bg=self.fg_color, 
                                     width=3, relief='flat', command=self.choose_fg_color)
        self.fg_color_btn.pack(side='right')
        

        bg_color_frame = ttk.Frame(color_frame, style='Custom.TFrame')
        bg_color_frame.pack(fill='x', padx=10, pady=(5, 10))
        
        ttk.Label(bg_color_frame, text="Background Color:", style='Custom.TLabel').pack(side='left')
        self.bg_color_btn = tk.Button(bg_color_frame, text="⬜", bg=self.bg_color,
                                     width=3, relief='flat', command=self.choose_bg_color)
        self.bg_color_btn.pack(side='right')
        

        logo_frame = ttk.LabelFrame(parent, text="Logo Options", style='Custom.TFrame')
        logo_frame.pack(fill='x', pady=(0, 10))
        
        self.logo_btn = ttk.Button(logo_frame, text="📁 Upload Logo", 
                                  command=self.upload_logo, style='Custom.TButton')
        self.logo_btn.pack(fill='x', padx=10, pady=(10, 5))
        
        self.logo_info = ttk.Label(logo_frame, text="No logo selected", style='Custom.TLabel')
        self.logo_info.pack(padx=10, pady=(0, 5))
        
        self.remove_logo_btn = ttk.Button(logo_frame, text="❌ Remove Logo", 
                                         command=self.remove_logo, style='Custom.TButton')
        self.remove_logo_btn.pack(fill='x', padx=10, pady=(0, 10))
        

        action_frame = ttk.Frame(parent, style='Custom.TFrame')
        action_frame.pack(fill='x', pady=(10, 0))
        
        self.generate_btn = ttk.Button(action_frame, text="🔄 Generate QR Code", 
                                      command=self.generate_qr, style='Custom.TButton')
        self.generate_btn.pack(fill='x', pady=(0, 5))
        
        self.save_btn = ttk.Button(action_frame, text="💾 Save QR Code", 
                                  command=self.save_qr, style='Custom.TButton')
        self.save_btn.pack(fill='x')
    
    def create_preview_panel(self, parent):
        """Create the preview panel"""
        preview_frame = ttk.LabelFrame(parent, text="QR Code Preview", style='Custom.TFrame')
        preview_frame.pack(fill='both', expand=True, padx=10)
        
        self.canvas = tk.Canvas(preview_frame, bg='white', relief='flat')
        self.canvas.pack(fill='both', expand=True, padx=20, pady=20)
        

        self.root.after(100, self.generate_qr)
    
    def on_text_change(self, event=None):

        if hasattr(self, '_text_change_timer'):
            self.root.after_cancel(self._text_change_timer)
        self._text_change_timer = self.root.after(500, self.generate_qr)
    
    def choose_fg_color(self):

        color = colorchooser.askcolor(color=self.fg_color, title="Choose Foreground Color")
        if color[1]:
            self.fg_color = color[1]
            self.fg_color_btn.config(bg=self.fg_color)
            self.generate_qr()
    
    def choose_bg_color(self):

        color = colorchooser.askcolor(color=self.bg_color, title="Choose Background Color")
        if color[1]:
            self.bg_color = color[1]
            self.bg_color_btn.config(bg=self.bg_color)
            self.generate_qr()
    
    def upload_logo(self):
        """Upload a logo image"""
        file_path = filedialog.askopenfilename(
            title="Select Logo Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
  
                with Image.open(file_path) as img:
                    img.verify()
                
                self.logo_path = file_path
                filename = os.path.basename(file_path)
                self.logo_info.config(text=f"Logo: {filename}")
                self.generate_qr()
                
            except Exception as e:
                messagebox.showerror("Error", f"Invalid image file: {str(e)}")
    
    def remove_logo(self):

        self.logo_path = None
        self.logo_info.config(text="No logo selected")
        self.generate_qr()
    
    def generate_qr(self, event=None):

        try:

            content = self.text_entry.get('1.0', tk.END).strip()
            if not content:
                content = "Hello, World!"
            

            error_levels = {
                "Low (7%)": qrcode.constants.ERROR_CORRECT_L,
                "Medium (15%)": qrcode.constants.ERROR_CORRECT_M,
                "Quartile (25%)": qrcode.constants.ERROR_CORRECT_Q,
                "High (30%)": qrcode.constants.ERROR_CORRECT_H
            }
            

            module_drawers = {
                "Square": SquareModuleDrawer(),
                "Rounded": RoundedModuleDrawer(),
                "Circle": CircleModuleDrawer()
            }
            

            qr = qrcode.QRCode(
                version=1,
                error_correction=error_levels.get(self.error_correction.get(), 
                                                qrcode.constants.ERROR_CORRECT_M),
                box_size=10,
                border=4,
            )
            
            qr.add_data(content)
            qr.make(fit=True)
            
            module_drawer = module_drawers.get(self.module_style.get(), SquareModuleDrawer())
            

            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            fg_rgb = hex_to_rgb(self.fg_color)
            bg_rgb = hex_to_rgb(self.bg_color)
            
            color_mask = SolidFillColorMask(back_color=bg_rgb, front_color=fg_rgb)
            
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=module_drawer,
                color_mask=color_mask
            )
            img.save(f"QR-CODE{time.time()}.png")
            

            if self.logo_path and os.path.exists(self.logo_path):
                img = self.add_logo_to_qr(img, self.logo_path)
            
            self.current_qr_image = img
            self.display_qr_image(img)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")
    
    def add_logo_to_qr(self, qr_img, logo_path):

        try:

            logo = Image.open(logo_path)
            
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width, qr_height) // 5
            

            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            logo_bg = Image.new('RGBA', (logo_size + 20, logo_size + 20), self.bg_color)
            
            logo_pos = ((logo_bg.width - logo.width) // 2, (logo_bg.height - logo.height) // 2)
            if logo.mode == 'RGBA':
                logo_bg.paste(logo, logo_pos, logo)
            else:
                logo_bg.paste(logo, logo_pos)

            qr_img = qr_img.convert('RGBA')
            logo_pos_qr = ((qr_width - logo_bg.width) // 2, (qr_height - logo_bg.height) // 2)
            qr_img.paste(logo_bg, logo_pos_qr, logo_bg)
            
            return qr_img.convert('RGB')
            
        except Exception as e:
            print(f"Error adding logo: {e}")
            return qr_img
    
    def display_qr_image(self, img):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            self.root.after(100, lambda: self.display_qr_image(img))
            return
        
        img_width, img_height = img.size
        max_size = min(canvas_width - 40, canvas_height - 40, 400)
        
        if img_width > max_size or img_height > max_size:
            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

        self.qr_photo = ImageTk.PhotoImage(img)
        
        self.canvas.delete("all")
        canvas_center_x = canvas_width // 2
        canvas_center_y = canvas_height // 2
        
        self.canvas.create_image(canvas_center_x, canvas_center_y, 
                               image=self.qr_photo, anchor="center")
    
    def save_qr(self):
        if not self.current_qr_image:
            messagebox.showwarning("Warning", "Please generate a QR code first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                high_res_qr = self.generate_high_res_qr()
                high_res_qr.save(file_path)
                messagebox.showinfo("Success", f"QR code saved successfully!\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {str(e)}")
    
    def generate_high_res_qr(self):
        content = self.text_entry.get('1.0', tk.END).strip()
        if not content:
            content = "Hello, World!"
        
        error_levels = {
            "Low (7%)": qrcode.constants.ERROR_CORRECT_L,
            "Medium (15%)": qrcode.constants.ERROR_CORRECT_M,
            "Quartile (25%)": qrcode.constants.ERROR_CORRECT_Q,
            "High (30%)": qrcode.constants.ERROR_CORRECT_H
        }
        
        module_drawers = {
            "Square": SquareModuleDrawer(),
            "Rounded": RoundedModuleDrawer(),
            "Circle": CircleModuleDrawer()
        }
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=error_levels.get(self.error_correction.get(), 
                                            qrcode.constants.ERROR_CORRECT_M),
            box_size=20,  
            border=4,
        )
        
        qr.add_data(content)
        qr.make(fit=True)
        
        module_drawer = module_drawers.get(self.module_style.get(), SquareModuleDrawer())
        

        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        fg_rgb = hex_to_rgb(self.fg_color)
        bg_rgb = hex_to_rgb(self.bg_color)
        
        color_mask = SolidFillColorMask(back_color=bg_rgb, front_color=fg_rgb)
        
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=module_drawer,
            color_mask=color_mask
        )
        
        if self.logo_path and os.path.exists(self.logo_path):
            img = self.add_logo_to_qr(img, self.logo_path)
        
        return img
    
    def toggle_theme(self):

        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme()
        self.save_settings()
    
    def apply_theme(self):

        theme = self.dark_theme if self.is_dark_theme else self.light_theme
        
        self.root.configure(bg=theme['bg'])
        
        self.theme_btn.config(text="☀️ Light Mode" if self.is_dark_theme else "🌙 Dark Mode")

        self.text_entry.config(
            bg=theme['entry_bg'],
            fg=theme['entry_fg'],
            insertbackground=theme['fg']
        )
        

        self.canvas.config(bg=theme['entry_bg'])

        self.configure_styles()

        self.root.update_idletasks()
    
    def center_window(self):

        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def load_settings(self):
        try:
            if os.path.exists('qr_settings.json'):
                with open('qr_settings.json', 'r') as f:
                    settings = json.load(f)
                    self.is_dark_theme = settings.get('dark_theme', False)
                    self.fg_color = settings.get('fg_color', '#000000')
                    self.bg_color = settings.get('bg_color', '#FFFFFF')
        except Exception:
            pass
    
    def save_settings(self):
        try:
            settings = {
                'dark_theme': self.is_dark_theme,
                'fg_color': self.fg_color,
                'bg_color': self.bg_color
            }
            with open('qr_settings.json', 'w') as f:
                json.dump(settings, f)
        except Exception:
            pass

def main():
    root = tk.Tk()
    app = QRCodeGenerator(root)
    
    # Handle window closing
    def on_closing():
        app.save_settings()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()