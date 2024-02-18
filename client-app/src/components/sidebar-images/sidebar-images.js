import React from "react";
import './sidebar-images.css'

const SidebarImages = props => {
    let url = props.url;
    console.log(url);

    return (
        <div className="sidebar container">
            Here will be images
        </div>
    )
}

export default SidebarImages;