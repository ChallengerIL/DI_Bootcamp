const UserFavoriteColors = (props) => {
    return (
        props.favAnimals.map((animal, index) => (
            <li key={index}>{animal}</li>
        ))
    )
}

export default UserFavoriteColors;