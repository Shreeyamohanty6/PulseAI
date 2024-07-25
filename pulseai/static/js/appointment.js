document.addEventListener('DOMContentLoaded', (event) => {
  // Get the date input element
  const dateInput= document.querySelector('input[name="date"]')
  const form = document.getElementById('appointmentForm');

  const today = new Date();
  const dd = String(today.getDate()).padStart(2, '0');
  //console.log(dd);
  const mm = String(today.getMonth() + 1).padStart(2, '0');
  const yyyy = today.getFullYear();
  const todayStr = `${yyyy}-${mm}-${dd}`;
  //console.log(todayStr)

  // Calculate the date 7 days from today
  const sevenDaysFromToday = new Date(today);
  sevenDaysFromToday.setDate(today.getDate() + 7);
  //console.log(sevenDaysFromToday);
  const dd7 = String(sevenDaysFromToday.getDate()).padStart(2, '0');
  const mm7 = String(sevenDaysFromToday.getMonth() + 1).padStart(2, '0');
  const yyyy7 = sevenDaysFromToday.getFullYear();
  const maxDateStr = `${yyyy7}-${mm7}-${dd7}`;
  //console.log(maxDateStr);

  // Set the min and max attributes of the date input
  dateInput.setAttribute('min', todayStr);
  dateInput.setAttribute('max', maxDateStr);

  form.addEventListener('submit', (event) => {
      const mobileInput = document.getElementById('mobile');
      const mobileValue = mobileInput.value;
      const mobileError = document.getElementById('mobileError');
      let error = false;

      // Validate mobile number
      if (mobileValue.length !== 10 || !/^\d{10}$/.test(mobileValue)) {
          mobileError.textContent = "Mobile Number must be 10 digits.";
          mobileInput.style.border = "1px solid red";
          error = true;
      } else {
          mobileError.textContent = "";
          mobileInput.style.border = "";
      }

      if (error) {
          event.preventDefault();
      }
  });
});

function confirmDelete(event) {
  let res = confirm("Are you sure, you want to delete?");
  if (!res) {
      event.preventDefault();
  }
}