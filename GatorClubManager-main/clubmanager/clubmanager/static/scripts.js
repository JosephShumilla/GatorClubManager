function addSocialMedia(){
    // Get the container where input boxes are appended
    const container = document.getElementById("formBox");

    // Create a new input element
    const input = document.createElement("input");
    input.type = "url";  // URL input type for social media links
    input.name = "social_media[]";  // Use array syntax to send multiple inputs
    input.placeholder = "Enter Social Media URL";

    // Optionally, create a label or line break before each input
    const br = document.createElement("br");

    // Append the input and line break to the container
    container.appendChild(br);  // Add a line break
    container.appendChild(input);  // Add the new input
    
}