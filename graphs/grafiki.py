import matplotlib.pyplot as plt
import numpy as np

# Данни от твоите тестове
tests = ['#1 Съзнание', '#2 Часовник', '#3 Математика', '#4 Емоции', 
         '#5 Философия', '#6 Техника', '#7 Сравнителен', '#8 Хумор', 
         '#9 Етика', '#10 Мета']

# Метрики
clean_perplexity = [49.73, 38.47, 30.90, 64.99, 49.98, 45.10, 224.07, 171.60, 41.27, 153.89]
analog_perplexity = [28.27, 15.33, 11.68, 26.49, 8.16, 13.02, 133.50, 30.16, 30.16, 40.80]

clean_token = [17.50, 14.75, 17.13, 11.81, 12.25, 13.38, 10.56, 10.69, 12.06, 10.50]
analog_token = [6.63, 5.03, 5.31, 3.27, 3.81, 3.75, 1.89, 1.80, 1.80, 2.83]

clean_attention = [22.74, 26.57, 23.94, 27.90, 27.90, 27.21, 31.81, 30.80, 27.21, 30.33]
analog_attention = [31.67, 40.37, 28.97, 41.35, 42.07, 42.62, 58.99, 57.22, 57.22, 51.14]

x = np.arange(len(tests))
width = 0.35

# ========== ГРАФИКА 1: Perplexity ==========
fig, ax = plt.subplots(figsize=(14, 7))
bars1 = ax.bar(x - width/2, clean_perplexity, width, label='Чист модел', color='#E74C3C')
bars2 = ax.bar(x + width/2, analog_perplexity, width, label='Аналогов модел', color='#2ECC71')
ax.set_ylabel('Perplexity (по-ниско = по-добре)', fontsize=12)
ax.set_title('Сравнение на Perplexity при 10 теста', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(tests, rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('perplexity_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# ========== ГРАФИКА 2: Token Repurposing ==========
fig, ax = plt.subplots(figsize=(14, 7))
bars1 = ax.bar(x - width/2, clean_token, width, label='Чист модел', color='#E74C3C')
bars2 = ax.bar(x + width/2, analog_token, width, label='Аналогов модел', color='#2ECC71')
ax.set_ylabel('Token Repurposing (по-ниско = по-добре)', fontsize=12)
ax.set_title('Сравнение на Token Repurposing при 10 теста', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(tests, rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('token_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# ========== ГРАФИКА 3: Attention Layer 2 ==========
fig, ax = plt.subplots(figsize=(14, 7))
bars1 = ax.bar(x - width/2, clean_attention, width, label='Чист модел', color='#E74C3C')
bars2 = ax.bar(x + width/2, analog_attention, width, label='Аналогов модел', color='#2ECC71')
ax.set_ylabel('Attention Layer 2 (по-високо = по-добре)', fontsize=12)
ax.set_title('Сравнение на Attention Layer 2 при 10 теста', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(tests, rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('attention_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# ========== ГРАФИКА 4: Три метрики в едно (радар) ==========
print("🎯 ГРАФИКИТЕ СА ГОТОВИ! Потърси ги като PNG файлове в папката.")