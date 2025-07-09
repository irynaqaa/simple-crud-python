import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * This class is responsible for handling user-related operations.
 */
@Service
public class UserService {

    private final UserRepository userRepository;

    /**
     * Constructs a new UserService instance.
     * @param userRepository the user repository to use
     */
    @Autowired
    public UserService(final UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    /**
     * Retrieves a list of all users.
     * @return a list of users
     */
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    /**
     * Retrieves a user by its ID.
     * @param id the ID of the user to retrieve
     * @return the user with the specified ID
     */
    public User getUserById(final Long id) {
        return userRepository.findById(id).orElse(null);
    }

    /**
     * Creates a new user.
     * @param user the user to create
     * @return the created user
     */
    public User createUser(final User user) {
        return userRepository.save(user);
    }

    /**
     * Updates an existing user.
     * @param user the updated user
     * @return the updated user
     */
    public User updateUser(final User user) {
        return userRepository.save(user);
    }

    /**
     * Deletes a user by its ID.
     * @param id the ID of the user to delete
     */
    public void deleteUser(final Long id) {
        userRepository.deleteById(id);
    }
}