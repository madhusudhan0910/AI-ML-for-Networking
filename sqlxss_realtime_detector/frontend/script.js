document.addEventListener("DOMContentLoaded", () => {
  const payloadForm = document.getElementById("threat-form");
  const payloadInput = document.getElementById("payload");
  const payloadResult = document.getElementById("payload-result");
  const payloadError = document.getElementById("payload-error");
  payloadForm?.addEventListener("submit", async (e) => {
    e.preventDefault();
    payloadResult.innerHTML = "";
    payloadError.innerText = "";
    const payload = payloadInput.value.trim();
    if (!payload) {
      payloadError.innerText = "Please enter a payload.";
      return;
    }
    const formData = new FormData();
    formData.append("payload", payload);
    try {
      const res = await fetch("/detect/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        const result = data.result.toLowerCase();
        payloadResult.innerHTML = `✅ Detection Result: <span class="tag tag-${result}">${result.toUpperCase()}</span>`;
      } else {
        payloadError.innerText = data.detail || "❌ Error occurred.";
      }
    } catch (err) {
      payloadError.innerText = "⚠️ Server connection failed.";
      console.error("Payload detection error:", err);
    }
  });
  const fileForm = document.getElementById("file-form");
  const fileInput = document.getElementById("file-input");
  const fileResult = document.getElementById("file-result");
  const fileError = document.getElementById("file-error");
  fileForm?.addEventListener("submit", async (e) => {
    e.preventDefault();
    fileResult.innerHTML = "";
    fileError.innerText = "";
    const file = fileInput.files[0];
    if (!file) {
      fileError.innerText = "Please upload a .txt or .csv file.";
      return;
    }
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await fetch("/detect_file/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        fileResult.innerHTML = `<strong>📂 Results from <em>${data.filename}</em></strong><br><br>`;
        data.results.forEach((entry, i) => {
          const label = entry.result.toLowerCase();
          fileResult.innerHTML += `${i + 1}. <code>${entry.payload}</code> — <span class="tag tag-${label}">${label.toUpperCase()}</span><br>`;
        });
      } else {
        fileError.innerText = data.detail || "❌ Error processing file.";
      }
    } catch (err) {
      fileError.innerText = "⚠️ Server connection failed.";
      console.error("File detection error:", err);
    }
  });
});
