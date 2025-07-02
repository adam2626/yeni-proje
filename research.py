research_data = {
    "python": "Python, Guido van Rossum tarafından geliştirilen yüksek seviyeli bir programlama dilidir.",
    "flask": "Flask, Python için hafif bir web framework'üdür.",
    "yapay zeka": "Yapay zeka, makinelerin insan benzeri zeka sergilemesini sağlar."
}

def perform_research(query):
    """Anlık araştırma yapar ve sonucu döndürür."""
    words = query.lower().split()
    for word in words:
        if word in research_data:
            return research_data[word]
    # Yeni bir şey öğrenmiş gibi simüle et
    new_info = f"{query} hakkında şu an öğrendim: Bu ilginç bir konu!"
    research_data[words[-1]] = new_info  # Yeni bilgiyi kaydet
    return new_info