
import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 24,
    gap: 200,
    backgroundColor: "black",
  },

  title: {
    fontSize: 32,
    fontWeight: "bold",
    marginBottom: 12,
    textAlign: "center",
  },

  subtitle: {
    fontSize: 16,
    textAlign: "center",
    marginBottom: 40,
    lineHeight: 24,
  },

  button: {
    width: "60%",
    height: 52,
    borderRadius: 10,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "white",
  },

  logo: {
    width: 100,
    height: 100,
    marginBottom: 24,
  },

  buttonText: {
    fontSize: 16,
    fontWeight: "600",
    color: "black",
  },
});
