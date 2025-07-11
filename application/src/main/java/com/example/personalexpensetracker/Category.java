/**
 * This class represents a category.
 */
public final class Category {
    private int id;
    private String name;
    private String description;
    /**
     * Constructs a new Category object.
     * @param id the category's ID
     * @param name the category's name
     * @param description the category's description
     */
    public Category(int id, String name, String description) {
        this.id = id;
        this.name = name;
        this.description = description;
    }
    /**
     * Gets the category's ID.
     * @return the category's ID
     */
    public int getId() {
        return id;
    }
    /**
     * Sets the category's ID.
     * @param id the new ID
     */
    public void setId(int id) {
        this.id = id;
    }
    /**
     * Gets the category's name.
     * @return the category's name
     */
    public String getName() {
        return name;
    }
    /**
     * Sets the category's name.
     * @param name the new name
     */
    public void setName(String name) {
        this.name = name;
    }
    /**
     * Gets the category's description.
     * @return the category's description
     */
    public String getDescription() {
        return description;
    }
    /**
     * Sets the category's description.
     * @param description the new description
     */
    public void setDescription(String description) {
        this.description = description;
    }
}
