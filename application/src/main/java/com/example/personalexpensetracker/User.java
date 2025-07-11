import java.util.Date;
/**
 * This class represents a user.
 */
public final class User {
    private int id;
    private String username;
    private String password;
    /**
     * Constructs a new User object.
     * @param id the user's ID
     * @param username the user's username
     * @param password the user's password
     */
    public User(int id, String username, String password) {
        this.id = id;
        this.username = username;
        this.password = password;
    }
    /**
     * Gets the user's ID.
     * @return the user's ID
     */
    public int getId() {
        return id;
    }
    /**
     * Sets the user's ID.
     * @param id the new ID
     */
    public void setId(int id) {
        this.id = id;
    }
    /**
     * Gets the user's username.
     * @return the user's username
     */
    public String getUsername() {
        return username;
    }
    /**
     * Sets the user's username.
     * @param username the new username
     */
    public void setUsername(String username) {
        this.username = username;
    }
    /**
     * Gets the user's password.
     * @return the user's password
     */
    public String getPassword() {
        return password;
    }
    /**
     * Sets the user's password.
     * @param password the new password
     */
    public void setPassword(final String password) {
        this.password = password;
    }
}
