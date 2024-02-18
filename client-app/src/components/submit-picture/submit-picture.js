import React, { useState } from "react";
import './submit-picture.css';

const SubmitPicture = props => {
    const [selectedFile, setSelectedFile] = useState(null);
    let url = props.url;

    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
    };

    const sendData = (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('image', selectedFile);

        const response = fetch(url, {
            method: 'POST',
            body: formData,
        });

    }

    return (
        <div className="submit_picture container">
            <form onSubmit={sendData}>
                <label for="image_uploads">Choose images to upload (PNG, JPG)</label>
                <br />
                <input
                    type="file"
                    accept=".jpg, .jpeg, .png"
                    onChange={handleFileChange} />
                <br />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default SubmitPicture;