let toastTimer;

function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');

  if (!toastComponent) return;

  // Hapus class tipe sebelumnya
  toastComponent.classList.remove('toast-success', 'toast-error', 'toast-normal');

  // Terapkan class baru berdasarkan tipe
  if (type === 'success') {
      toastComponent.classList.add('toast-success');
  } else if (type === 'error') {
      toastComponent.classList.add('toast-error');
  } else {
      toastComponent.classList.add('toast-normal');
  }

  // Perbarui konten teks
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Batalkan timer sebelumnya jika toast masih tampil
  clearTimeout(toastTimer);

  // Animasi muncul
  if (!toastComponent.matches(':popover-open')) {
      toastComponent.showPopover();
      void toastComponent.offsetHeight; // paksa browser menghitung style agar transisi berjalan
  }
  toastComponent.classList.remove('toast-hidden');
  toastComponent.classList.add('toast-show');

  // Animasi hilang otomatis
  toastTimer = setTimeout(() => {
      toastComponent.classList.remove('toast-show');
      toastComponent.classList.add('toast-hidden');
      toastTimer = setTimeout(() => toastComponent.hidePopover(), 300);
  }, duration);
}

// Fungsi showToast memiliki empat parameter:
// title adalah judul notifikasi yang akan ditampilkan.
// message adalah pesan utama yang akan ditampilkan.
// type adalah tipe notifikasi (seperti 'success', 'error' atau 'normal'). Parameter ini menentukan skema warna notifikasi.
// duration adalah durasi notifikasi muncul di layar (dalam milidetik).

// Fungsi ini secara dinamis mengubah kelas CSS dan konten elemen HTML berdasarkan parameter yang diberikan. Secara rinci, showToast melakukan langkah-langkah berikut:

// Fungsi ini mengakses elemen-elemen HTML toast melalui ID-nya, yaitu toast-component, toast-title, dan toast-message.
// Fungsi ini menghapus kelas-kelas tipe sebelumnya untuk memastikan notifikasi memiliki gaya yang benar sebelum menerapkan gaya yang baru.
// Fungsi ini menambahkan kelas CSS yang sesuai (toast-success, toast-error atau toast-normal) untuk mengubah warna border berdasarkan parameter type.
// Fungsi ini memperbarui teks judul dan pesan notifikasi.
// Fungsi ini menampilkan toast dengan showPopover() agar toast berada di top layer browser, di atas elemen lain termasuk modal. Setelah itu, fungsi ini menghapus kelas toast-hidden dan menambahkan kelas toast-show sehingga toast tampak muncul dari bawah layar.
// Fungsi ini menggunakan setTimeout untuk menyembunyikan toast secara otomatis setelah durasi yang ditentukan, lalu memanggil hidePopover() setelah animasinya selesai. clearTimeout membatalkan timer sebelumnya agar toast yang dipanggil berturut-turut tidak disembunyikan terlalu cepat.
