import matplotlib.pyplot as plt
import numpy as np

tests = ['#1','#2','#3','#4','#5','#6','#7','#8','#9','#10']
clean_logit = [14.06, 15.44, 12.50, 13.69, 13.81, 13.50, 13.44, 12.56, 14.69, 17.88]
analog_logit = [14.06, 18.50, 13.00, 16.75, 18.38, 12.63, 12.94, 12.56, 12.56, 28.00]

x = np.arange(len(tests))
width = 0.35

fig, ax = plt.subplots(figsize=(14, 7))
bars1 = ax.bar(x - width/2, clean_logit, width, label='Чист модел', color='#E74C3C')
bars2 = ax.bar(x + width/2, analog_logit, width, label='Аналогов модел', color='#2ECC71')

ax.set_ylabel('Logit Variance (по-високо = по-разнообразен)', fontsize=12)
ax.set_title('Сравнение на Logit Variance при 10 теста', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(tests, rotation=45, ha='right')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('logit_variance_comparison.png', dpi=300, bbox_inches='tight')
plt.show()