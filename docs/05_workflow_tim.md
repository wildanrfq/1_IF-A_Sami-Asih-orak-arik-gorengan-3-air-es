# Panduan Kerja Tim

## Git
- Branch: `main` (stabil), `feat/<nama-fitur>`, `docs/<topik>`.
- Commit singkat dan jelas, contoh: `feat: tambah stabilitas ARI`.
- Buka Pull Request, minimal 1 anggota me-review sebelum merge.
- Jangan commit data mentah dan hasil besar (sudah diatur di `.gitignore`).

## Notebook
- Jalankan **Restart and Run All** sebelum commit agar output konsisten.
- Logika yang dipakai ulang dipindah ke `src/rfm_kmeans/`, bukan disalin antar notebook.

## Checklist sebelum submit
- [ ] `pytest -q` lulus
- [ ] Notebook 01 dijalankan penuh, angka dan grafik masuk laporan bagian 2.4 dan 2.5
- [ ] Atribusi dataset ada di Daftar Pustaka
- [ ] Tautan repositori di Lampiran B benar
