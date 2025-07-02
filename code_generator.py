code_templates = {
    "merhaba dünya": "print('Merhaba, Dünya!')",
    "sayıları topla": "def topla(a, b):\n    return a + b",
    "liste oluştur": "my_list = [1, 2, 3, 4, 5]"
}

def generate_code(task):
    """İstenen göreve göre kod üretir."""
    task = task.lower().strip()
    if task in code_templates:
        return code_templates[task]
    # Yeni bir şablon simüle et
    new_code = f"# {task} için basit bir kod\nprint('{task} yapıldı!')"
    code_templates[task] = new_code
    return new_code