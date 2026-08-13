const API = window.location.origin;

const urlInput = document.getElementById("url");
const audioBtn = document.getElementById("audio");
const videoBtn = document.getElementById("video");
const status = document.getElementById("status");

audioBtn.addEventListener("click", () => {
    download("mp3");
});

videoBtn.addEventListener("click", () => {
    download("mp4");
});

async function download(type) {

    const url = urlInput.value.trim();

    if (!url) {
        alert("Enter YouTube URL");
        return;
    }

    status.innerText = "Downloading... Please wait.";

    try {

        const response = await fetch(
            `${API}/download/${type}?url=${encodeURIComponent(url)}`
        );

        if (!response.ok) {
            throw new Error("Download failed");
        }

        const blob = await response.blob();

        let filename =
            type === "mp3"
                ? "audio.mp3"
                : "video.mp4";

        const disposition = response.headers.get("Content-Disposition");

        if (disposition) {

            const match = disposition.match(/filename="?([^"]+)"?/);

            if (match) {
                filename = match[1];
            }
        }

        const blobUrl = window.URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = blobUrl;
        a.download = filename;

        document.body.appendChild(a);

        a.click();

        a.remove();

        window.URL.revokeObjectURL(blobUrl);

        status.innerText = "Download Complete.";

    } catch (err) {

        console.error(err);

        status.innerText = "Download Failed.";
    }
}