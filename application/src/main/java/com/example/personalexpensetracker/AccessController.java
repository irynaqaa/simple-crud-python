import java.util.HashMap;
import java.util.Map;
public class AccessController {
    private Map<String, Role> roles;

    public AccessController() {
        roles = new HashMap<>();
        roles.put("admin", Role.ADMIN);
        roles.put("user", Role.USER);
    }

    public boolean hasAccess(String username, String resource) {
        Role role = roles.get(username);
        if (role == Role.ADMIN) {
            return true;
        } else if (role == Role.USER) {
            return resource.equals("transactions");
        } else {
            return false;
        }
    }
}
