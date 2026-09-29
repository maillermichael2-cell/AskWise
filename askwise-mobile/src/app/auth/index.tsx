import { View, Text, StyleSheet, Pressable, Image } from "react-native";
import {styles} from "../../styles/auth.styles";
import {router} from "expo-router";

export default function AuthScreen() {
  return (
    <View style={styles.container}>

      <Image
        source={require("../../../assets/images/expo-logo.png")}
        style={styles.logo}
      />

      <Pressable style={styles.button} onPress={() => router.replace("/(tabs)")}>
        <Text style={styles.buttonText}>Continue with Google</Text>
      </Pressable>

    </View>
  );
}