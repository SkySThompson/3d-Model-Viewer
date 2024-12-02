// Function to fetch and display the list of uploaded models
function viewUploadHistory() {
    const historyMenu = document.getElementById('historyMenu');
    const uploadsList = document.getElementById('uploadsList');
  
    // Clear the current list before fetching new data
    uploadsList.innerHTML = '';
  
    // Fetch uploaded models from Flask API
    fetch('/get_uploads')
      .then(response => response.json())
      .then(data => {
        if (data.uploads && data.uploads.length > 0) {
          // Loop through the uploaded models and create a list
          data.uploads.forEach(modelUrl => {
            const listItem = document.createElement('li');
            const modelLink = document.createElement('a');
            modelLink.href = modelUrl;  // Link to the uploaded model
            modelLink.textContent = modelUrl; // Show the URL of the model
            listItem.appendChild(modelLink);
            uploadsList.appendChild(listItem);
          });
        } else {
          // If no models are uploaded, show a message
          uploadsList.innerHTML = '<li>No models uploaded yet.</li>';
        }
  
        // Show the history menu when data is fetched
        historyMenu.style.display = 'block';
      })
      .catch(error => {
        console.error('Error fetching upload history:', error);
      });
  }
  
  // Attach event listener to the history button
  document.getElementById('historyButton').addEventListener('click', viewUploadHistory);
  