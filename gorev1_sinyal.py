"""
BIL216 İşaretler ve Sistemler - 2025-2026 Bahar Dönemi
Ödev 1 - GÖREV 1: Sinüzoidal İşaretlerin Örneklenmesi ve Görselleştirilmesi

Grup Parametresi:
  Son iki haneler: 20, 26, 62
  f0 = 20 + 26 + 62 = 108 Hz
"""

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# PARAMETRELER
# ─────────────────────────────────────────────
f0 = 108          # Temel frekans (Hz)
f1 = f0           # 108 Hz
f2 = f0 / 2       # 54  Hz
f3 = 10 * f0      # 1080 Hz

# Örnekleme Frekansı Seçimi (Nyquist Kriteri)
# En yüksek frekans f3 = 1080 Hz
# Nyquist: fs >= 2 * f_max => fs >= 2160 Hz
# Güvenli temsil için fs = 10 * f3 = 10800 Hz seçildi.
# Bu seçim, f3 sinyalini periyot başına 10 örnek ile temsil eder
# ve aliasing (örtüşme) bozulmasını tamamen önler.
fs = 10 * f3      # 10800 Hz

# ─────────────────────────────────────────────
# ZAMAN EKSENLERİ (Her sinyal için en az 3 tam periyot)
# ─────────────────────────────────────────────
num_periods = 3

def make_time(freq):
    """Verilen frekans için 3 periyot kapsayan zaman dizisi üretir."""
    T = 1.0 / freq
    t_end = num_periods * T
    return np.arange(0, t_end, 1.0 / fs)

t1 = make_time(f1)
t2 = make_time(f2)
t3 = make_time(f3)

# ─────────────────────────────────────────────
# SİNYALLER
# ─────────────────────────────────────────────
x1 = np.sin(2 * np.pi * f1 * t1)
x2 = np.sin(2 * np.pi * f2 * t2)
x3 = np.sin(2 * np.pi * f3 * t3)

# Toplam sinyal: ortak zaman ekseni (en uzun periyota göre = f2)
t_sum = make_time(f2)
x_sum = (np.sin(2 * np.pi * f1 * t_sum) +
         np.sin(2 * np.pi * f2 * t_sum) +
         np.sin(2 * np.pi * f3 * t_sum))

# ─────────────────────────────────────────────
# GRAFİKLER — 3 alt grafik (subplot) aynı pencerede
# ─────────────────────────────────────────────
fig, axes = plt.subplots(3, 1, figsize=(12, 8))
fig.suptitle(
    f"BIL216 Ödev 1 – GÖREV 1\n"
    f"f₀ = {f0} Hz  |  Örnekleme Frekansı: fs = {int(fs)} Hz",
    fontsize=13, fontweight='bold'
)

plot_data = [
    (t1, x1, f1, "f₁ = f₀",       "#1f77b4"),
    (t2, x2, f2, "f₂ = f₀ / 2",   "#2ca02c"),
    (t3, x3, f3, "f₃ = 10 × f₀",  "#d62728"),
]

for ax, (t, x, freq, label, color) in zip(axes, plot_data):
    ax.plot(t * 1000, x, color=color, linewidth=1.2)  # zaman eksenini ms cinsinden göster
    ax.set_title(f"{label} = {freq:.0f} Hz", fontsize=11)
    ax.set_xlabel("Zaman (ms)")
    ax.set_ylabel("Genlik")
    ax.set_xlim([t[0] * 1000, t[-1] * 1000])
    ax.set_ylim([-1.3, 1.3])
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("gorev1_subplot.png", dpi=150, bbox_inches='tight')
plt.show()

# ─────────────────────────────────────────────
# TOPLAM SİNYAL — Ayrı pencerede
# ─────────────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.plot(t_sum * 1000, x_sum, color="#7b2d8b", linewidth=1.2)
ax2.set_title(
    f"Toplam Sinyal: x(t) = sin(2π·{f1:.0f}t) + sin(2π·{f2:.0f}t) + sin(2π·{f3:.0f}t)",
    fontsize=11
)
ax2.set_xlabel("Zaman (ms)")
ax2.set_ylabel("Genlik")
ax2.set_xlim([t_sum[0] * 1000, t_sum[-1] * 1000])
ax2.axhline(0, color='gray', linewidth=0.5, linestyle='--')
ax2.grid(True, alpha=0.3)

fig2.suptitle("BIL216 Ödev 1 – GÖREV 1 | Toplam Sinyal", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("gorev1_toplam.png", dpi=150, bbox_inches='tight')
plt.show()

print("✓ Grafikler kaydedildi: gorev1_subplot.png, gorev1_toplam.png")
print(f"\n── Parametre Özeti ──")
print(f"  f₀ = {f0} Hz")
print(f"  f₁ = {f1:.0f} Hz  →  T₁ = {1/f1*1000:.2f} ms")
print(f"  f₂ = {f2:.0f} Hz  →  T₂ = {1/f2*1000:.2f} ms")
print(f"  f₃ = {f3:.0f} Hz  →  T₃ = {1/f3*1000:.2f} ms")
print(f"  fs = {int(fs)} Hz  (Nyquist min: {int(2*f3)} Hz → {int(fs/f3):.0f}× güvenlik payı)")
