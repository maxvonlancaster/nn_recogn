import React from "react";
import './sidebar-images.css'

const SidebarImages = props => {
    let url = props.url;
    let request = fetch(url)
        .then(response => response.json())
        .then(data => console.log(data));
    console.log(url);

    return (
        <div className="sidebar container">
            Here will be images
        </div>
    )
}

export default SidebarImages;