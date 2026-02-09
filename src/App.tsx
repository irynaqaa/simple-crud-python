import React, { useEffect } from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  useNavigate,
  useLocation,
} from "react-router-dom";
import "./App.css";

export const deleteUser = async (userId: string): Promise<void> => {
  const response = await fetch(`/delete?userId=${encodeURIComponent(userId)}`, {
    method: "GET",
  });
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Delete request failed: ${errorText}`);
  }
};

const DeleteUser: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const userId = params.get("userId");
    if (!userId) {
      navigate("/", { replace: true });
      return;
    }

    const performDelete = async () => {
      try {
        await deleteUser(userId);
      } catch (error) {
        console.error(error);
      } finally {
        navigate("/", { replace: true });
      }
    };

    performDelete();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [location.search, navigate]);

  return null;
};

const UserList: React.FC = () => {
  return (
    <div>
      <h1>User List</h1>
      {/* List rendering logic goes here */}
    </div>
  );
};

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UserList />} />
        <Route path="/delete" element={<DeleteUser />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;

import React from "react";
import { render, waitFor } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import DeleteUser, { deleteUser } from "./App";

global.fetch = jest.fn();

jest.mock("react-router-dom", () => {
  const actual = jest.requireActual("react-router-dom");
  return {
    ...actual,
    useNavigate: () => jest.fn(),
  };
});

describe("DeleteUser component", () => {
  const mockNavigate = jest.fn();

  beforeEach(() => {
    (global.fetch as jest.Mock).mockReset();
    (require("react-router-dom").useNavigate as jest.Mock).mockReturnValue(
      mockNavigate
    );
  });

  it("calls deleteUser and navigates to root on success", async () => {
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: true,
    });

    render(
      <MemoryRouter initialEntries={["/delete?userId=123"]}>
        <Routes>
          <Route path="/delete" element={<DeleteUser />} />
        </Routes>
      </MemoryRouter>
    );

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        "/delete?userId=123",
        expect.objectContaining({ method: "GET" })
      );
      expect(mockNavigate).toHaveBeenCalledWith("/", { replace: true });
    });
  });

  it("handles fetch failure gracefully and still navigates", async () => {
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: false,
      text: async () => "Server error",
    });

    const consoleErrorSpy = jest.spyOn(console, "error").mockImplementation();

    render(
      <MemoryRouter initialEntries={["/delete?userId=456"]}>
        <Routes>
          <Route path="/delete" element={<DeleteUser />} />
        </Routes>
      </MemoryRouter>
    );

    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        "/delete?userId=456",
        expect.objectContaining({ method: "GET" })
      );
      expect(consoleErrorSpy).toHaveBeenCalled();
      expect(mockNavigate).toHaveBeenCalledWith("/", { replace: true });
    });

    consoleErrorSpy.mockRestore();
  });
});