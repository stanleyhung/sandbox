import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Wake {
	private final static String macAddress = "00.1D.60.88.57.46";
	private final static String networkAddress = "192.168.1.255";

	public static void main(String[] args) {

		byte[] macAddressBytes = getAddressBytes(macAddress, 16);
		byte[] bytes = new byte[6 + 16*macAddressBytes.length];

		for (int i = 0; i < 6; i++) {
			bytes[i] = (byte) 0xff;
		}

		for (int i = 6; i < bytes.length; i++) {
			bytes[i] = macAddressBytes[i % 6];
		}

		byte[] network = getAddressBytes(networkAddress, 10);
		for (int i = 0; i < network.length; i++) {
		}

		try {
			InetAddress ipAddress = InetAddress.getByAddress(network);
			DatagramPacket packet = new DatagramPacket(bytes, bytes.length, ipAddress,80);
			DatagramSocket socket = new DatagramSocket();
			socket.send(packet);
			socket.close();
		} catch (Exception e) {
			System.exit(1);
		}
	
	}

	private static byte[] getAddressBytes (String address, int radix) throws IllegalArgumentException {
		String[] string = address.split("\\.");
		byte[] bytes = new byte[string.length];

		for (int i = 0; i < string.length; i++) {
			bytes[i] = (byte) Integer.parseInt(string[i], radix);
		}

		return bytes;

	}

}