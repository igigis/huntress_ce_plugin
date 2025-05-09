# Huntress HEC Connector for Netskope Cloud Exchange

This connector enables the forwarding of events from Netskope Cloud Exchange to the Huntress HTTP Event Collector (HEC) endpoint.

## 📦 Files Included

- `main.py` – Main connector logic
- `manifest.json` – Plugin definition file
- `mappings.json` - mapped logs
- `README.md` – Setup and usage instructions

## 🔧 Configuration

When configuring the connector in Cloud Exchange, you'll need to provide:

- **token**: The Huntress HEC token
- **verify_ssl** *(optional)*: Set to `true` (default) to verify SSL certificates

> **Note**: The HEC URL is hardcoded to `https://hec.huntress.io/services/collector`. You do not need to provide this during configuration.

## ✅ Supported Operations

- **push_event**: Sends any JSON-formatted event to the Huntress HEC

## 🚀 How to Use

1. Place the connector files in a directory:
   ```
   huntress_ce_plugin/
   ├── main.py
   ├── manifest.json
   └── README.md
   ```

2. Zip the contents:
   ```bash
   zip -r huntress_ce_plugin.zip main.py manifest.json icon.png mappings.json CHANGELOG.md README.md 
   ```

3. Upload the `.zip` file to your Netskope Cloud Exchange portal under **Plugins** > **Add Plugin**.

4. Configure the plugin with your Huntress HEC token.

## 🧪 Testing

You can test the connector by sending a dummy payload:
```json
{
  "event": {
    "test": "huntress integration",
    "source": "netskope-ce"
  }
}
```

## 🛠 Troubleshooting

- Check Cloud Exchange logs for plugin output and error messages.
- Ensure your HEC token has the appropriate permissions.
- Set `verify_ssl` to `false` if you're testing with custom certs (not recommended for production).

## 📬 Support
For any issues or feedback, reach out to your Netskope or Huntress contact.
