import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
export default function sidebar({links, close}){
    return (
        <div className= "sidebar" onClick= {close}>
            { links.map(link => (
                <a className = "sidebar-link" href= "#!" key={link.name}>
                    <FontAwesomeIcon icon={link.name} />
                    {link.name}
                </a>

            ))}
        </div>
    )
}