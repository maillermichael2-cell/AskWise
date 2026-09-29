import { View, Text } from "react-native";
import { styles } from "../../styles/home.styles";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Askwise</Text>

      <Text style={styles.subtitle}>
        Ask questions and get answers from your knowledge base.
      </Text>
    </View>
  );
}