using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class UdpIntReceiver : MonoBehaviour
{
    public int port = 8765;
    private UdpClient udpClient;
    private IPEndPoint endPoint;
    private int receivedValue;
    public float MovementSpeed;

    void Start()
    {
        endPoint = new IPEndPoint(IPAddress.Any, port);
        udpClient = new UdpClient(port);

        Debug.Log("UDP Receiver listening on port " + port);
    }

    void Update()
    {
        // Check for available UDP packets
        while (udpClient.Available > 0)
        {
            byte[] data = udpClient.Receive(ref endPoint);
            string msg = Encoding.UTF8.GetString(data);

            if (int.TryParse(msg, out int value))
            {
                receivedValue = value;
                Debug.Log("Received: " + receivedValue);

                if (receivedValue > 0)
                    MoveObjectUp();
            }
        }
    }

    void MoveObjectUp()
    {
        transform.Translate(Vector3.up * MovementSpeed * Time.deltaTime);
        Debug.Log("Moved object up.");
    }

    void OnApplicationQuit()
    {
        udpClient?.Close();
    }
}
